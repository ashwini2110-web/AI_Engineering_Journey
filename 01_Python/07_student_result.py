print("==================\n"
"Student Result\n"
"==================\n")

name = input("Enter your name = ")
subject = ["physics", "maths", "english", "chem", "C"]
marks = []

# Taking inputs of student

for sub in subject:
    try:
        mark = int(input(f"Enter your marks in {sub} : "))
        if(mark>100):
            print("Enter marks between 1 to 100")
            break
        
        marks.append(mark)

    except ValueError:
        print("Invalid Input!! Enter Integer") 
        break

print("\n",marks)

# Definition of function

def calculate_avg(marks):
    total = sum(marks)
    average = total/len(marks)
    return total,average
    
# Calling of function

if(len(marks)==len(subject)):
    total,average = calculate_avg(marks)
    print(f"Total of marks is : {total}")
    print(f"Average of marks is : {average}\n")
    
#  Using conditions 

    if(average>=90):
        print("Outstanding")
    elif(average>=80):
        print("Very Good")    
    elif(average>=70):
        print("Good")    
    elif(average>=60):
        print("Can do better")    
    elif(average>=50):
        print("Needs to improve")    
    elif(average>=40):
        print("Pass")   
    elif(average>=35):
        print("Just Pass")
    else:
        print("Fail")    

print("==================")

