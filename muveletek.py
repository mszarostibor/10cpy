#kerekités mit hánytizedesre
"""
print(round(3.1415, 3))
print(round(3.1415, 2))
#hatványozás
print(pow(2, 8)) #alap, kitevő
#apszulutérték
print(abs(-12))
print(min(89, 3, 5))
print(max(75, 6, 56))
"""
#pi
"""
import math
a=math.pi
print(a)
"""
from math import *
"""
c=pi
print(c)
#négyzetgyök -sqrt math.sqrt
print(sqrt(16))
#felfelékerekités ceil
print(ceil(3.56))
#lefelekerekités floor
print(floor(3.56))
"""
#négyzet kerülete területe
#téglalap kerülete területe
#kör kerülete (2*r*pi) területe (r^2*pi)
#kocka V=a^3 A=6*a^2
#derékszögü háromszög 2 befogo bekérése a^2+b^2
a=float(input("irjon számot"))
b=float(input("irjon még egy számot"))
print("kerülete" a*4)
print("területe" a*a)
print("kerülete" pow(a, 2)+pow(b, 2))
print("területe" a*b)
r=float(input("irjon még számot"))
print(2*r*pi)
print("kerülete"pow(r, 2)*pi)
print("területe"pow(a, 3))
print("kerülete"pow(a, 2)*6)
print("területe"pow(a, 2)+pow(b, 2))