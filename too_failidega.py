from mumu import *
from os import *

laused=[] 
while True:
    menu=input("\n1-loeme failist \n2-Salvestame failisse \n3-Tekst helisse \n4-lulka \n")
    while menu.isdigit()==False:
        menu=input("Kirjuta ainult need numbrid, mis on ")
    print()
    if menu=="1":
        laused=loe("Laused.txt")
        for line in laused:
            print(line)
    elif menu=="2":
        line=input("Lisa lause: ")
        laused.append(line)
        kirjuta("Laused.txt",laused)
    elif menu=="3":
        text=""
        for line in laused:
            text=text+" "+line 
        heli(text,"ja")
    elif menu=="4":
        os.system("3.mp3")