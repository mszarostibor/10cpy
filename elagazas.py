def feladat1():
    a=int(input("Kérek egy egész számot! a="))
    if a%2==0:
        print("A megadott szám páros.")
    else:
        print("A megadott szám páratlan")

def feladat2(szam):
    if szam<0:
        print("negativ a szám")
    else:
        print("pozotiv a szám")
    
def feladat3(szam):
    if szam<0:
        print("nincs fagy")
    else:
        print("van fagy")

def feladat4(szam):
    if szam>-30 and szam<40:
        print("A megadott szám -30 és 40 közé esik")
    else:
        print("Nem esik a megadott intervallumba.")

def feladat5(szam):
    if szam<16:
        print(szam*10)
    else:
        print(szam/3)

def feladat6():
    a=int(input("kérek egy számot"))
    if 0<a and a<10:
        print("tizesek")
    elif 10<a and a<20:
        print("huszasok")
    elif 20<a and a<30:
        print("harmincasok")
    elif 30<a and a<40:
        print("negyvenesek")
    elif 40<a and a<50:
        print("ötvenesek")
    else 50<a:
        print("nincs a tartományban")

def feladat7():
    a=int(input("kérek egy számot"))
    if 12<a:
        print("nagyobb 12-nél")
    elif a<25:
        print("kisebb mint 25")
    elif a%2:
        print("páros")
    else:
        print(a,"nincs benne")

def feladat8():
    a=int(input("kérek egy számot"))
    if a<0:
        print("szilárd")
    elif 0<a and a<100:
        print("folyékony")
    else 100<a:
        print("gáz")

def feladat9(szam):
    if szam%3:
        print("osztható 3-mal")
    elif szam%4:
        print("osztható 4-el")
    elif szam%9:
        print("osztható 9-el")
    else:
        print("nemosztható a 3 vagy 4 vagy 9")

def feladat10(szam):
    if szam%4:
        print("szökőév")
    else:
        print("nem szökőév")

def feladat11():
    a=float(input("Kérem a háromszög a oldalát! a="))
    b=float(input("Kérem a háromszög b oldalát! b="))
    c=float(input("Kérem a háromszög c oldalát! c="))
    if a+b>c and a+c>b and b+c>a:
        print("A háromszög szerkeszthető.")
    else:
        print("A háromszög nem szerkeszthető.")

#Itt kezdődik a főprogram
#a=int(input("Kérek egy számot! a="))
#feladat1()
#feladat2()
#feladat3()
#feladat4(43)
#feladat4(34)
#feladat4(-30)
#feladat5(a)
#feladat6()
#feladat7()
#feladat8()
#feladat9()
#feladat10()
#feladat11();
