def feladat22():
    szorzok=[2, 3, 5, 7, 11, 13, 17, 19]
    for item in szorzok:
        for i in range(1,16):
            print(item*i, end=' ')
        print()

def feladat23():
    nevek=['JeanMichel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'AlexandreBenoît', 'Louise']
    hossz=[]
    for item in nevek:
        hossz.append(len(item))
        #print(item) ez is egy megoldás
        #print('szavak hossza',len(item))
    
    for i in range(0, len(nevek)):
        print(nevek[i],hossz[i])

def feladat24():
    szamok=[53,6,69,7,84,9,62,10,84,26,74,3,96,62,7,84,69]
    szamoka=[]
    for item in szamok:
        if item not in szamoka:
            szamoka.append(item)
    szamoka.sort()
    print(szamoka)

def feladat25():
    #mondat=input("kérek egy mondatot")
    mondat=" Írjon egy scriptet, ami megkeresi egy adott mondatban a leghosszabb szót (a program felhasználójának be kell tudnia írni egy általa választott mondatot)."
    print('szavak száma',mondat.count(' ')+1)
    print('mondat hossza',len(mondat))
    szavaka=mondat.split(' ')
    szavakhossza=[]
    print('szavak száma',len(szavaka))
    for item in szavaka:
        szavakhossza.append(len(item))
    leghosszabb=max(szavakhossza)
    indexe=szavakhossza.index(leghosszabb)
    print('leghosszabb szo',szavaka[indexe])
    #másik megoldás
    for item in szavaka:
        if len(item)==leghosszabb:
            print('leghosszabb szo',item)
    
def sajat():
    """a feladat az hogy írja ki a megadot mondatnak a hosszúságát és számolja meg az 'a' karaktert"""
    mondat='Nézd milyen csendes az olasz család a szomszéd asztalnál'
    print('a mondat hossza',len(mondat))
    print('a mondatban ennyi a van',mondat.count('a'))
#feladat22()
#feladat23()
#feladat24()
#feladat25()
sajat()