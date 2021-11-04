from random import *

def listaAlapok():
    alapok=[]
    for i in range(10):
        alapok.append(randint(1,50))
    alapok.append('alma')
    alapok.append('szilva')
    print(alapok)
    for item in alapok:
        print(item, end=" ")
    print()
    print(alapok[4]) #négyes indexü elem
    print(len(alapok))
    alapok.insert(4,"körte") #berakta az adott helyre
    #print(alapok.index(55))
    alapok.remove('körte')
    alapok.pop() #utolsó törlése
    del alapok[-1] #megadott törlése
    del alapok[1] #elsö törlése
    #alapok.clear() elemeket töröl
    #del alapok listát törli
    alapok.reverse() #megforditja
    alapok.sort() 
    alapok.reverse()
    print()
    print(alapok[5:]) #ötös indextöl a végéig 
    print(alapok[:4]) #negyedik ig
    print(alapok[-1]) #utolso
    print(alapok[-2]) #utolso elöti
    print(alapok[-2:]) #utolso kettö
    print(alapok[3:5])
    alapok[6]="narancs"
    print()
    for item in alapok:
        print(item, end=" ")
    print()

def feladat1():
    elemszam=int(input("add meg a számokat "))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok)
    paratlandb=0
    for item in szamok:
        if item%2==1:
            paratlandb+=1
    print("A páratlanok száma ",paratlandb)

def feladat2():
    elemszam=int(input("add meg a számokat "))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok)
    osszeg=0
    for item in szamok:
        if item%2==1:
            osszeg+item
    print("a párosok összege ",osszeg)

def feladat3():
    elemszam=int(input("add meg a számokat "))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok)
    for i in range(len(szamok)):
        if szamok[i]%2==0:
            print(i+1, '\t', szamok[i])


#listaAlapok()
#feladat1()
feladat2()