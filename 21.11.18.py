def megtalal(karakterlanc, keresendo):
    if keresendo in karakterlanc:
        return karakterlanc.index(keresendo)
    else:
        return -1

def karakterszam(karakterlanc, megszamolando):
    return karakterlanc.count(megszamolando)

def feladat2():
    szoveg='Lorem ipsum dolor sit amet consectetur adipisicing elit. At, omnis?'
    karakter=input('Adj karakter ')
    #kiiraás
    print(megtalal(szoveg, karakter))
    #változó
    eredmeny=megtalal(szoveg, karakter)
    if eredmeny==-1:
        print("Nem szerepel")
    else:
        print('a megadott karakter:', eredmeny,"fordul elő")

def feladat4():
    szoveg='Lorem ipsum dolor sit amet consectetur adipisicing elit. At, omnis?'
    karakter=input('Adj karakter ')
    karakterszam(szoveg, karakter)
    print("a megadot szövegben",karakterszam(szoveg, karakter),"alkalomal fordul elő")

def feladat5():
    prefixes='JKLMNOPQ'
    suffixe='ack'
    kacsak=[]
    for item in prefixes:
        kacsak.append(item+suffixe)
    for item in kacsak:
        print(item, end=' ')

def feladat6():
    szoveg='Lorem ipsum dolor sit amet consectetur adipisicing elit. At, omnis?'
    print("a megadot szoveg",karakterszam(szoveg, ' ')+1," szóbol áll")

def nagybetu():
    nagybetuk=
#itt kezdödik a főprogram
#feladat2()
#feladat4()
feladat5()
#feladat6()