import numpy as np

# Displaying Marks of student
marks = np.array([78, 65, 91, 55, 84, 72, 88, 69])
print(f"Marks of student are : {marks}")

# Total of marks
print(f"Total of marks are : {np.sum(marks)}")

# Average of marks
print(f"Average of marks is : {np.mean(marks)}")

# Highest of marks
print(f"Highest marks out of all marks is : {np.max(marks)}")

# Lowest of marks
print(f"Lowest marks out of all marks is : {np.min(marks)}")

# Marks greater than 75
marks_greater_75 = marks[marks > 75]
print(f"Marks greater than 75 are : {marks_greater_75}")

# Marks lower than 70
print(f"Marks lower than 70 are : {marks[marks < 70]}")

# Marks after adding 5 bonus marks
print(f"Marks after adding 5 bonus marks are : {np.add(marks, 5)}")

# marks sorted in ascending and descending order
print(f"Marks sorted in ascending order is : {np.sort(marks)}")
print(f"Marks sorted in descending order is : {np.sort(marks, descending = bool)}")

# Number of students who scored 75 or more
print(f"Number of students who scored 75 or more : {np.count_nonzero(marks >= 75)}")