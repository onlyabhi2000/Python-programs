num=int(input("enetr a number:"))
if num>1:
    for i in range(1,11):
        table=num*i
        print(table)
else:
    print("not acceptable")