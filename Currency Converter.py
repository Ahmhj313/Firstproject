import math
import random
# The currencies list
# It only converts from USD to one of these currencies
KWD = 0.303203
EUR = 0.822786
GBP = 0.733632
IRR = 41738.96
XBT = 0.0000264505 
# Choose the currency
y = input("Please insert the currency: ")
x = float(input("Please insert the value: "))
y = y.upper()
# Now let hte CPU do its' work ;)
if y=="KWD":
    z=round(x*KWD,2)
    z=str(z)
    print(z + " " + y)
if y=="EUR":
    z=round(x*EUR,2)
    z=str(z)
    print(z + " " + y)
if y=="GBP":
    z=round(x*GBP,2)
    z=str(z)
    print(z + " " + y)
if y=="IRR":
    z=round(x*IRR,2)
    toman = z*10**-1
    toman = str(toman)
    z=str(z)
    print(z + " " + y)
    print((toman + " " + "Toman"))
if y=="XBT":
    z=round(x*XBT,2)
    z=str(z)
    print(z + " " + "Bitcoin(s)")
    
