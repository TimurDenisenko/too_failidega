from gtts import *
from random import *
import os

def loe(x:str)->str:
    """
    opisanie
    """
    f=open(x,"r",encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip()) 
    f.close()
    return jarjend 

def kirjuta(x:str,y:list):
    """
    opisanie
    """
    f=open(x,"w",encoding="utf-8-sig")
    for line in y:
        f.write(line+"\n")
    f.close() 

def heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("chinano.mp3") 
    os.system("chinano.mp3")

def tolk(fail1:str,fail2:str):
    rus=[] 
    est=[]
    f=open(fail1,'r',encoding="utf-8-sig")
    for line in f:
        rus.append(line.strip())
    f.close()
    f=open(fail2,'r',encoding="utf-8-sig")
    for line in f:
        est.append(line.strip()) 
    f.close()
    sona=input("Kirjutage sõna, mida soovite tõlkida ")
    while sona.isdigit():
        sona=input("Kirjuta õige sõna")
    if sona not in rus and sona not in est:
        print("Seda sõna pole sõnastikus ")
        vale=input("Kas soovite selle sõna sõnaraamatusse lisada? (jah või ei) ").lower() 
        while vale not in ["jah","ei"]:
            vale=input("Kirjuta ainult jah või ei ") 
        if vale=="jah":
            keel=input("Kas see on vene keel või eesti keel? ").lower()
            while keel not in ["vene keel","eesti keel"]:
                keel=input("Kirjutage ainult vene keel või eesti keel ")
            if keel=="vene keel":
                f=open(fail1,'a',encoding="utf-8-sig") 
                f.write("\n"+sona) 
                f.close()
                tolke=input("Kirjutage sõna tõlge ") 
                while tolke.isdigit():
                    tolke=input("Kirjuta õige sõna ")
                f=open(fail2,"a",encoding="utf-8-sig")
                f.write("\n"+tolke) 
                f.close()
            else: 
                f=open(fail2,'a',encoding="utf-8-sig") 
                f.write("\n"+sona) 
                f.close()
                tolke=input("Kirjutage sõna tõlge ") 
                while tolke.isdigit():
                    tolke=input("Kirjuta õige sõna ")
                f=open(fail1,"a",encoding="utf-8-sig")
                f.write("\n"+tolke) 
                f.close()
        else:
            print("Olgu, hüvasti")
    for i in range(len(rus)):
        if sona==rus[i]:
            print(f"{rus[i]} - {est[i]}")
            heli(est[i],"et")
        elif sona==est[i]:
            print(f"{est[i]} - {rus[i]}")
            heli(rus[i],"ru") 

def paranda(fail1:str,fail2:str):
    rus=[] 
    est=[]
    f=open(fail1,'r',encoding="utf-8-sig")
    for line in f:
        rus.append(line.strip())
    f.close()
    f=open(fail2,'r',encoding="utf-8-sig")
    for line in f:
        est.append(line.strip()) 
    f.close()
    keel=input("Kas parandame vene või eesti sõnaraamatus? ").lower()
    while keel not in ["vene","eesti"]:
        keel=input("Kirjuta vene või eesti ")
    if keel=="vene":
        indv=input("Millist sõna soovite parandada? ")
        while indv not in rus:
            indv=input("Kirjutage õige sõna ")
        for i in range(len(rus)):
            if indv==rus[i]:
                ind=rus.index(indv) 
        parasona=input("Kirjutage parandatud sõna ")
        while parasona.isdigit():
            parasona=input("Kirjutage õige sõna ")
        rus[ind]=parasona
        for i in range(len(rus)):
            rus[i]=rus[i]+"\n"
        f=open(fail1,"w",encoding="utf-8-sig")
        f.writelines(rus)
        f.close()
    else:
        indv=input("Millist sõna soovite parandada? ")
        while indv not in est:
            indv=input("Kirjutage õige sõna ")
        for i in range(len(rus)):
            if indv==est[i]:
                ind=est.index(indv) 
        parasona=input("Kirjutage parandatud sõna ")
        while parasona.isdigit():
            parasona=input("Kirjutage õige sõna ")
        est[ind]=parasona
        for i in range(len(rus)):
            est[i]=est[i]+"\n"
        f=open(fail2,"w",encoding="utf-8-sig")
        f.writelines(est)
        f.close()

def harjutus(fail1:str,fail2:str):
    rus=[] 
    est=[]
    game=[] 
    a=[]
    v=k=0
    f=open(fail1,'r',encoding="utf-8-sig")
    for line in f:
        rus.append(line.strip())
    f.close()
    f=open(fail2,'r',encoding="utf-8-sig")
    for line in f:
        est.append(line.strip()) 
    f.close() 
    for i in range(len(rus)):
        num=randint(0,(len(rus)-1))
        while num in a:
            num=randint(0,(len(rus)-1))
        keel=input("Mis keeles treenime? (vene või eesti) ").lower()
        while keel not in ["vene","eesti"]:
            keel=input("Kirjutage ainult vene või eesti ").lower() 
        if keel=="vene":
            rana=rus[num] 
            tolk=input(f"Mis on sõna {rana} tõlge? ") 
            if tolk==est[num]:
                game.append(f"{i+1} {keel} mäng - võit")
                print("Võit") 
                v+=1
            else:
                game.append(f"{i+1}, {keel} mäng - kaotus") 
                print("Kaotus")
                k+=1
        else:
            rana=est[num] 
            tolk=input(f"Mis on sõna {rana} tõlge? ") 
            if tolk==rus[num]:
                game.append(f"{i+1} {keel} mäng - võit")
                print("Võit")
                v+=1
            else:
                game.append(f"{i+1}, {keel} mäng - kaotus") 
                print("Kaotus")
                k+=1
        a.append(num)
    print(game)
    resV=round((v/len(rus)*100),1)
    resK=round((k/len(rus)*100),1)
    print(f"Võiduprotsent - {resV}")
    print(f"Kaotusprotsent - {resK}")
