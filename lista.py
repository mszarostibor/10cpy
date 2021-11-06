from random import *

def listaAlapok():
    # lista létrehozása
    alapok=[]
    for i in range(10):
        alapok.append(randint(1,50))
    alapok.append('alma') # elem hozzáadása
    alapok.append('szilva') # elem hozzáadása
    print(alapok)
    # lista kiírása szépen
    for item in alapok:
        print(item, end=" ")
    print()
    print(alapok[4]) # 4-es indexű elem (sorban az ötödik)
    print(len(alapok)) # lista elemszáma
    alapok.insert(4,"körte") #elem beszúrása adott helyre
    print(alapok.index('körte')) # elem indexe
    #print(alapok.index(55)) # hibaüzenettel áll meg, ha nincs benne
    alapok.remove('körte') # elem törlése
    alapok.pop() # utolsó törlése
    del alapok[-1] # utolsó törlése
    del alapok[1] # 1-es indexű törlése
    #alapok.clear() # lista elemeket törli, lista megmarad
    #del alapok # listát törli
    alapok.reverse() # sorrendet megfordítja
    alapok.sort() # növekvő sorrend
    alapok.reverse()
    print()
    print(alapok[5:]) # 5-ös indextől a végéig
    print(alapok[:4]) # elejétől az adott indexűig(ezt már nem)
    print(alapok[-1]) # utolsó
    print(alapok[-2]) # utolsó előtti
    print(alapok[-2:]) # utolsó kettő
    print(alapok[3:5])
    alapok[6]='narancs'
    print(alapok[6])
    print()
    for item in alapok:
        print(item, end=" ")
    print()

def feladat1():
    elemszam=int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok) # ellenőrzés miatt
    paratlandb=0
    for item in szamok:
        if item%2==1:
            paratlandb+=1 # paratlandb=paratlandb+1
    print('A páratlanok száma',paratlandb)    

def feladat2():
    elemszam=int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok) # ellenőrzés miatt
    osszeg=0
    for item in szamok:
        if item%2==0:
            osszeg+=item
    print("A párosok összege", osszeg)

def feladat3():
    elemszam=int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok) # ellenőrzés miatt
    for i in range(len(szamok)):
        if szamok[i]%2==0:
            print(i+1, '\t', szamok[i])

def feladat5():
    elemszam=float(input("Add meg az elemek számát!"))
    szamok=[]
    szam=float(input("Add meg a számot"))
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok) # ellenőrzés miatt
    for i in range(szamok):
        if szamok==szamok:
            print("1")

def feladat6():
    elemszam=input("Add meg az tanulok nevét")
    szamok=[]
    szemely=input("személy")
    for i in range(elemszam):
    print(szamok) # ellenőrzés miatt
    for i in range(szamok):
        if szamok[i]==1:
            print("van", szemely)

#listaAlapok()
#feladat1()
#feladat2()
#feladat3()
#feladat5()
#feladat6()