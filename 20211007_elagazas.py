def feladat1():
    a=int(input("kérek egésszám: "))
    if a%2==0:
        print("páros")
    else:
        print("páratlan")
def feladat4(szam):
    if szam>-30 and szam<40:
        print("a szám -30 és 40 közé esik")
    else:
        print("nem esik az intervallumba")
def feladat5(szam):
    if szam<16:
        print(szam*10)
    else:
        print(szam/3)

#a=int(input("kérek számot "))
def feladat11():
    a = float(input("kérem a szám a oldalát "))
    b = float(input("kérem a szám b oldalát "))
    c = float(input("kérem a szám c oldalát "))
    if a+b>c and a+c>b and b+c>a:
        print("szerkeszthető")
    else:
        print("nem szerkeszthető")

#feladat1()
#feladat4(43)
#feladat4(34)
#feladat4(-30)
#feladat5(a)
feladat11()