from mumu import *
from os import *

laused=[] 
while True:
    menu=input("""
1-loeme failist \n2-Salvestame failisse \n3-Tekst helisse \n4-Sõnade tõlkimine \n5-Vaata sõnastikku
6-Parandage viga sõnastikus\n7-Harjutus\n
""")
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
        tolk("rus.txt","est.txt")
    elif menu=="5":
        laused=loe("rus.txt")
        for line in laused:
            print(line)
        print()
        laused=loe("est.txt")
        for line in laused:
            print(line)
    elif menu=="6":
        paranda("rus.txt","est.txt")
    elif menu=="7":
        harjutus("rus.txt","est.txt")