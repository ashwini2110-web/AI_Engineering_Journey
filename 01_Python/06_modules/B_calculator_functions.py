# Function Definition

def add(num1, num2):
        return num1+num2

def sub(num1, num2):
        return num1-num2

def mul(num1, num2):
        return num1*num2

def div(num1, num2):
        return num1/num2

def rem(num1, num2):
        return num1%num2

# Funtion Call 
try:
    num1 = int(input("Enter first number = "))
    num2 = int(input("Enter second number = "))
    op = int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Remainder\n"
    "Enter the operation you want to perform = "))

    match op:
        case 1:
            print(f"Addition of {num1} and {num2} is = {add(num1, num2)}")

        case 2:
            print(f"Subtraction of {num1} and {num2} is = {sub(num1, num2)}")

        case 3:
            print(f"Multiplication of {num1} and {num2} is = {mul(num1, num2)}")

        case 4:
            print(f"Division of {num1} and {num2} is = {div(num1, num2)}") 

        case 5:
            print(f"Remainder of {num1} and {num2} is = {rem(num1, num2)}")       

except:
      print("Invalid input!! Enter integer type value")

print("Change your value and try again")      
