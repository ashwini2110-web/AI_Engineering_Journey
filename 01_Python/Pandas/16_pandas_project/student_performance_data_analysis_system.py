import pandas as pd
import numpy as np
# Importing student_data csv file
student_data = pd.read_csv("16_pandas_project/student_performance.csv")
print(student_data)

# Data Inspection
print("Top-most row of student-data is : ")
print(student_data.head(1))
print("Last row of student-data is : ")
print(student_data.tail(1))
print("Basic information about student : ")
print(student_data.info())
print("Basic description about student : ")
print(student_data.describe())
print("Shape of student-data : ",student_data.shape)
print("Columns in student-data : ",student_data.columns)

# Data Cleaning
print("Checking null characters in dataset : ")
print(student_data.isnull())
print("Filling mean values in place of Null : ")
print(student_data["Math"].fillna(student_data["Math"].mean()))  
print(student_data["Science"].fillna(student_data["Science"].mean()))  
print(student_data["English"].fillna(student_data["English"].mean()))  
print("Droping rows with null characters : ")
print(student_data.dropna())
print("Students with duplicated marks :")
print(student_data.duplicated())
print("Droping duplicated marks : ")
print(student_data.drop_duplicates())

# Datatype Fixing
student_data["Date_of_Birth"] = ["2005-15-3","2005-22-7","2004-11-12","2006-3-5","2005-28-8","2006-19-1","2004-25-9","2005-10-4","2004-30-11","2006-14-2","2005-22-7",
                                "2005-18-6","2004-7-10","2005-21-1","2006-12-8","2004-29-5","2005-16-9","2005-4-12","2006-23-3","2004-8-7","2005-17-10","2005-15-3"]
student_data["Date_of_Birth"] = pd.to_datetime(student_data["Date_of_Birth"], format = "%Y-%d-%m")
student_data["DOB_Int"] = student_data["Date_of_Birth"].astype("int64")
student_data["Birth_Day"] = student_data["Date_of_Birth"].dt.day
student_data["Birth_Month"] = student_data["Date_of_Birth"].dt.month
student_data["Birth_Year"] = student_data["Date_of_Birth"].dt.year
student_data["Weekday"] = student_data["Date_of_Birth"].dt.day_name()
print(student_data)

# Total Marks and Percentage calculation
student_data["Total_Marks"] = student_data["Math"] + student_data["Science"] + student_data["English"]
print("Total and Percentage of student : ")
student_data["Percentage"] = student_data["Total_Marks"] / 300 * 100
print(student_data)
def grade(Percentage):
    if Percentage >= 90:
        return "A"
    elif Percentage >= 75:
        return "B"
    elif Percentage >= 60:
        return "C"
    elif Percentage >= 40:
        return "D"
    else:
        return "Fail"
student_data["Grade"] = student_data["Percentage"].apply(grade)
print(student_data)

# Filtering
print("Students with 'A' Grade :")
print(student_data.loc[student_data["Grade"] == "A"])
print("Students with low attendance :")
print(student_data.loc[student_data["Attendance"] < 75])
print("Students living in Pune :")
print(student_data.loc[student_data["City"] == "Pune"])

# Sorting
print("Top 10 students :")
print(student_data.sort_values(by = "Percentage", ascending = False).head(10))
print("Lowest 10 students :")
print(student_data.sort_values("Percentage").head(10))

# Grouping
print("Average Marks by City : ")
print(student_data.groupby("City")["Total_Marks"].mean())
print("Average Marks by Class : ")
print(student_data.groupby("Class")["Total_Marks"].mean())
print("Number of students in each grade : ")
print(student_data.groupby("Grade")["Grade"].value_counts())
print("Number of students in each city : ")
print(student_data.groupby("City")["City"].value_counts())

# Exporting Data
cleaned_students = student_data.to_csv("cleaned_students.csv", index = False) 

# Summary Report
print("Summary Report of Student Data : ")
print(f"Total Students : {student_data['Name'].count()}")
print(f"Highest Score : {student_data['Total_Marks'].max()}")
print(f"Lowest Score : {student_data['Total_Marks'].min()}")
print(f"Average Percentage : {student_data['Percentage'].mean()}")
print(f"Topper of class : {student_data.sort_values(by = 'Total_Marks', ascending = False)["Name"].head(1)}")
print(f"Most Common Grade : {student_data['Grade'].mode()[0]}")
print(f"Students below 75% Attendents : {student_data.loc[student_data['Attendance'] < 75]["Attendance"].count()}")
print("Top 3 Cities by Average Marks :")
print(student_data.groupby("City")["Total_Marks"].mean().sort_values(ascending = False))