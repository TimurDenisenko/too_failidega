from gtts import *
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

def tolk(text:str,keel:str):
    for 