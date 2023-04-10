num=int(input("enetr a number:"))
x=0
y=1
for i in range(1,num+1):
    fibbo=x+y
    x=y
    y=fibbo
    print(y)