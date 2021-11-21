def megtalal(karakterlanc, keresendo):
    if keresendo in karakterlanc:
        return karakterlanc.index(keresendo)
    else:
        return -1

def karakterszam(karakterlanc, megszamolando):
    return karakterlanc.count(megszamolando)

def feladat2():
    szoveg='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Accusamus, qui?'
    karakter=input('Adj meg egy karaktert!')
    # kiírjuk a visszakapott eredményt
    print(megtalal(szoveg, karakter))
    # változóba tesszük
    eredmeny=megtalal(szoveg,karakter)
    if eredmeny==-1:
        print("A megadott karakter nem szerepel a szövegben")
    else:
        print('A megadott karakter a', eredmeny, 'indexű helyen fordul elő először.')

def feladat4():
    szoveg='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Accusamus, qui?'
    karakter=input('Adj meg egy karaktert!')
    print('A megadott szövegben az adott karakter',karakterszam(szoveg, karakter), 'alkalommal fordul elő')

def feladat6():
    szoveg='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Accusamus, qui?'
    print('A megadott szöveg', karakterszam(szoveg, ' ')+1,'szóból áll.')

def feladat5():
    prefixes='JKLMNOPQ'
    suffixe='ack'
    kacsak=[]
    for item in prefixes:
        kacsak.append(item+suffixe)
    for item in kacsak:
        print(item, end=' ')

def feladat7():
    szoveg='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Accusamus, qui?'
    nagybetu=['AÁBCDEÉFGHIJKLYMNOÓÖŐPQRSSZTTYUÚÜŰVWXYZZS']
    if nagybetu in szoveg:
        True
    else:
        False

def feladat10():
    szoveg='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Accusamus, qui?'
    szavak = szoveg.split()
    print(szavak)

#itt kezdődik a főprogram
#feladat2()
#feladat4()
#feladat5()
#feladat6()
#feladat7()
feladat10()