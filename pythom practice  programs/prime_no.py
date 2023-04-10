num=int(input("enetr a number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("non-prime no:")
            break
    else:
        print("prime no:")
