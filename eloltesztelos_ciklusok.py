def feladat24():
    szam=float(input("kérek egy számot "))
    while szam!=0:
        szam=float(input("kérek egy számot kilépés 0 "))

def feladat25():
    szam=float(input("kérek egy pozitiv számot "))
    while szam<=0:
        szam=float(input("a számod negativ "))

def feladat26():
    szam=float(input("szám "))
    oszeg=szam
    while szam<10:
        szam=float(input("szám "))
        oszeg+=szam
    print("beadot számok összege ",oszeg)
        







#feladat24()
#feladat25()
feladat26()