
list_elements = list(map(int, input("Enter elements of the list : ").split()))
print(list_elements)

# Finding Maximum out of a list using functions without using max()

def maximum(list_elements):
    max_value = list_elements[0]
    for num in list_elements:
        if num > max_value:
            max_value = num     
    return max_value

print("Maximum from given list is : ",maximum(list_elements))
student_name = str(input("Enter your name : "))
student_branch = str(input("Enter your branch : "))
student_marks = list(map(float, input("Enter your marks : ").split( )))
student_subjects = input("Enter your subjects : ").split( )
student_dict = dict(zip(student_subjects, student_marks))

# Displaying student's information

def display():
    print(student_name)
    print(student_branch)
    print(student_subjects)
    print(student_marks)
    print(student_dict)

# Finding average of student's marks

def average(student_marks):
    sum = 0
    for i in range(0,len(student_marks)):
        sum += student_marks[i]
    avg = float(sum / len(student_marks))  
    return avg

# Determining whether student is pass or fail

def result(avg):
    if avg >= 35.0:
        print("You Passed!!")
    else:
        print("You Failed. Better luck next time")   

# Calling functions

avg = average(student_marks)
display()
print("Average of you marks is : ", average(student_marks))
result(avg)


