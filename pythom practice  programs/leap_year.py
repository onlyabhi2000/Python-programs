year=int(input("enetr a year:"))
if (year%4==0) and (year%100!=0):
    print("leap year")
else:
    print("Not a leap year")
