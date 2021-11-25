from random import *

def feladat1():
    szamok=[]
    for i in range(20, 41):
        szamok.append(i**2)

def feladat2():
    szoveg="Az ősz annyira szereti a naplementéket, hogy minden egyes levélre egyet fest."
    print(len(szoveg))
    darab = 0
    szavak = szoveg.split()
    print('hogy hány szóból áll', szavak)
    for e in szoveg:
        if e == "e":
            darab += 1
        return darab
    szam=[]
    magánhanzok=['aáeéiíoóöőuúüű']
    if magánhanzok in szoveg:
        szam.append(1)
    print(szam)

def feladat3():
    szamok=[]
    osszeg=0
    atlag=0
    oszthatok=[]
    for i in range(15):
        szamok.append(randint(1,100))   
    for szam in szamok:
        osszeg += szam
        atlag += szam / len(szamok)
    legnagyobb=max(szamok)
    legkisebb=min(szamok)
    terjedelme = legnagyobb - legkisebb
    for item in szamok:
        if item %3 == 0:
            oszthatok.append(item)
    print('Ezek a számok osszthatok hárommal', oszthatok)
