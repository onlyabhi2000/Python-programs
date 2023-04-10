
num = int(input ("Enter the number of terms: "))

result = list (map (lambda x: 2 ** x, range (num)))

print("The total number of terms are:", num)

for i in range (num):

              print ("2 raised to the power", i, "is", result [i])
