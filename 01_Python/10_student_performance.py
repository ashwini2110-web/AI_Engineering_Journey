# Displaying student details and calculation of marks 
# using *args and **kwargs

print("================================\n" \
      "      Student Performance\n" \
      "================================")

# Student details
subject = ["English", "Physics", "Chemistry", "Biology", "Maths"]
values = []
for sub in subject:
    marks = int(input(f"Enter marks of {sub} : "))
    values.append(marks)

students = {"Name": "Ashwini",
            "Branch": "AIDS",
            "Goal": "Data Scientist",
            "marks": [mark for mark in values]}

print(f"Marks of student are as follows : {values}")

# function to calculate total marks of student

def total_marks(*marks):
    total = 0
    for mark in marks:
        total += mark
    return total

# function to calculate average marks of student

def average_marks(*marks):
    total = total_marks(*marks)
    average = total / len(marks)
    print(f"Average Marks : {average}")
    return average

# Finding highest and lowest marks without using max() or min()

highest = values[0]
for mark in values:
    if mark > highest:
        highest = mark
print(f"Maximum Marks : {highest}")

lowest = values[0]
for mark in values:
    if mark < lowest:
        lowest = mark
print(f"Minimum Marks : {lowest}")

total = total_marks(*students["marks"])
print(f"Total Marks : {total}")
average_marks(*students["marks"])

# Finding marks greater than 75

greater_75 = [mark for mark in values if mark > 75]
print(f"Marks greater than 75 : {greater_75}")

# Finding square of every mark

square = [mark**2 for mark in values]
print(f"Square of marks : {square}")


