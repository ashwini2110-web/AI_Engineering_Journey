import matplotlib.pyplot as plt
import pandas as pd

# Student data with percentage
csv_file = pd.read_csv("C:/Users/Ashwini/Documents/GitHub/AI_Engineering_Journey/01_Python/Pandas/16_pandas_project/cleaned_students.csv")
csv_file["Math"] = csv_file["Math"].fillna(csv_file["Math"].mean())
csv_file["Science"] = csv_file["Science"].fillna(csv_file["Science"].mean())
csv_file["English"] = csv_file["English"].fillna(csv_file["English"].mean())
csv_file["Total_Marks"] = (
    csv_file["Math"]
    + csv_file["Science"]
    + csv_file["English"]
)
csv_file["Percentage"] = (
    csv_file["Total_Marks"] / 300
) * 100
print(csv_file)
name = csv_file["Name"]
percent= csv_file["Percentage"]
plt.figure(figsize = (6,4))
plt.bar(name, percent)
plt.xticks(rotation=80)
plt.title("Student Percentage")
plt.xlabel("Students")
plt.ylabel("Percentage")

# Displaying Toppers of class - using bar chart
plt.figure(figsize = (6,4))
top_10 = csv_file.sort_values(by="Percentage",ascending=False).head(10)
plt.bar(top_10["Name"], top_10["Percentage"], width = 0.6, color = "Green")
plt.xticks(rotation=45)
plt.title("Top 10 Students")
plt.xlabel("Students")
plt.ylabel("Percentage")

# Subject Comparison - using line chart
math = csv_file["Math"]
sci = csv_file["Science"]
eng = csv_file["English"]
plt.figure(figsize = (6,4))
plt.plot(name, math, label = "Marks of Maths", color = "blue", marker = "o")
plt.plot(name, sci, label = "Marks of Science", color = "green", marker = "o")
plt.plot(name, eng, label = "Marks of English", color = "red", marker = "o")
plt.legend()
plt.xticks(rotation=80)
plt.title("Subject-wise Comparison")
plt.xlabel("Students")
plt.ylabel("Subjects")

# Attendance Distribution - using histogram chart
attendance = csv_file["Attendance"]
plt.figure(figsize = (6,4))
plt.hist(attendance, bins = 10)
plt.title("Attendance Distribution")

# City-wise Performance - using bar chart
plt.figure(figsize = (6,4))
percent = csv_file.groupby("City")["Percentage"].mean()
print(percent)
plt.bar(percent.index, percent.values, color="purple", width = 0.4)
plt.title("City-wise Performance")
plt.ylabel("Average Total Marks")
plt.xlabel("Cities")

# Grade Distribution - using pie chart
grades = ["A", "B", "C", "D", "Fail"]
grade_counts = csv_file["Grade"].value_counts()
plt.figure(figsize=(6,4))
plt.pie(grade_counts.values, labels=grade_counts.index, autopct="%1.1f%%")
plt.title("Grade Distribution")

# Attendance VS Percentage - using Scatter plot
plt.figure(figsize = (6,4))
percentage = csv_file["Percentage"]
plt.scatter(attendance, percentage, color = "green")
plt.title("Attendance VS Percentage")
plt.xlabel("Attendance")
plt.ylabel("Percentage")

# Dashboard - using subplot
plt.figure(figsize = (12,8))
# subplot-1 : Top Students
plt.subplot(2,2,1)
plt.bar(top_10["Name"], top_10["Percentage"], width = 0.6, color = "Green")
plt.xticks(rotation=80)
plt.title("Top 10 Students")
plt.xlabel("Students")
plt.ylabel("Percentage")
# subplot-2 : Grade Distribution
plt.subplot(2,2,2)
plt.pie(grade_counts.values, labels=grades, autopct="%1.1f%%")
plt.title("Grade Distribution")
# subplot-3 : Attendance Histogram
plt.subplot(2,2,3)
plt.hist(attendance, bins = 10)
plt.title("Attendance Distribution")
# subplot-4 : Attendance VS Percentage
plt.subplot(2,2,4)
plt.scatter(attendance, percentage, color = "green")
plt.title("Attendance VS Percentage")
plt.xlabel("Attendance")
plt.ylabel("Percentage")
plt.tight_layout()
plt.show()
