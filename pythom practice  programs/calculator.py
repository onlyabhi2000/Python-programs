
def add(number_1, number_2):
    return number_1 + number_2
  
def subtract(number_1, number_2):
    return number_1 - number_2
  
def multiply(number_1, number_2):
    return number_1 * number_2
  
def divide(number_1, number_2):
    return number_1 / number_2

print("Please select -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
        

operation = int(input("kripya choose kre"))
  
number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
  
if operation == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
  
elif operation == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
  
elif operation == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
  
elif operation == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Please enter Valid input")
 
