a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
ch = int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Remainder\nEnter your choice : "))

def choice(ch):
    match ch:

        case 1:
            print("Addition is = ",a+b)
        case 2:
            print("Subtraction is = ",a-b)
        case 3:
            print("Multiplication is = ",a*b)
        case 4:
            print("Division is = ",a/b)
        case 5:
            print("Remainder is = ",a%b)

if(ch == 1):
    choice(1)
elif(ch == 2):
    choice(2)
elif(ch == 3):
    choice(3)
elif(ch == 4):
    choice(4)    
elif(ch == 5):
    choice(5)


