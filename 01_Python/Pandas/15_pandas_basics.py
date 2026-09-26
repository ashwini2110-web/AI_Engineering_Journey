import pandas as pd

# Creating Dataframes
df_1 = pd.DataFrame([1,2,3,4], columns = ["Col_1"])
print(f"Dataframe is : \n{df_1}")
print(type(df_1))
data = {
    "Name" : ["Ashwini", "Disha", "Abhishek", "Sourav", "Vaishnavi"],
    "Age" : [20, 16, 20, 14, 14],
    "Std" : ["2nd year", "1st year", "2nd year", "10th", "10th"]
}
df_2 = pd.DataFrame(data)
print(f"Dataframe is : \n{df_2}")

# Basic Dataframe Understanding
print("Top 2 rows are : ")
print(df_2.head(2))           # gives Top 2 rows
print("Last 2 rows are : ")
print(df_2.tail(2))           # gives Last 2 rows
print("Shape of DataFrame is : ",df_2.shape)         # (rows, columns)
print("Columns in DataFrame are : ",df_2.columns)    # Prints all columns
print("Renaming Column 'Std' as 'Class' : \n", df_2.rename(columns = {"Std":"Class"}))
print("Basic information regarding DataFrame is : ")
df_2.info()
print("Basic description of DataFrame is : ")
print(df_2.describe())

# Save and Load data from csv
student_data = {
    "Roll_no" : [1,2,3,4,5,6,7,8,9,10],
    "Name" : ["a","b","c","d","e","f","g","h","i","j"],
    "Marks" : [80,79,60,90,96,98,95,57,67,54]
}
df_3 = pd.DataFrame(student_data)
print(f"DataFrame is : \n{df_3}")
# print(f"Discription is : \n{df_3.describe()}")
# df_3.to_csv("Pandas_data.csv", index = False)  # exports csv file
# read = pd.read_csv("Pandas_data.csv")          # imports csv file
# print(read)

# Rows and Columns - Selection
# Selecting a column
print(df_3[["Name","Roll_no"]])   # two columns are selected and printed
# Selecting a row
# Loc - Label based index
print(df_3.loc[df_3.Name=="a"])   # single row is selected
print(df_3.loc[0:3])              # multiple rows are selected
# iloc - index-value based index
print(df_3.iloc[0])               # single row 
print(df_3.iloc[0:3])             # multiple rows

# Filter dataframe
print(df_3["Marks"] > 70)         # gives boolean value
print(df_3[(df_3["Marks"] > 70) & (df_3["Roll_no"] >= 5)])   # gives actual value          
print(df_3.where(df_3["Marks"] >= 70))             # gives NaN to places where condition is not valid

# Rows and Columns - Operations (Add, update, delete)
# Adding new column
df_3["Subjects"] = ["Math", "Eng", "Bio", "Phy", "Chem", "BXE", "BEE", "EM", "DS", "AI"]
print(df_3)
df_3["Percentage"] = df_3["Marks"] * 100 / 110
print(df_3)
# Adding new row
df_3.loc[len(df_3)] = [11, "k", 34, "DELD", 34 * 100 / 110]
print(df_3)
# Updating value - Using index name
df_3.loc[0, "Marks"] = 85
df_3.loc[0, "Percentage"] = 85 * 100 / 110
print(df_3)
# Updating valur - Using column value
df_3.loc[df_3.Name == "b", "Marks"] = 85
df_3.loc[df_3.Name == "b", "Percentage"] = 85 * 100 / 110
print(df_3)
# Deleting value
# Deleting row
print(df_3.drop(df_3[df_3.Name == "a"].index))
# Deleting columns
print(df_3.drop(["Percentage","Subjects"], axis=1))
print(df_3.drop(0, axis = 0))    # Deleting row - Using index value
print(df_3.drop("Percentage", axis = 1))     # Deleting column - Using index value
# Sorting value
print(df_3.sort_values("Percentage"))    # Ascending order
print(df_3.sort_values("Percentage", ascending = False))                       # Decending order

# Working with data value
df_3["Exam_Date"] = ["2006-30-09", "2006-14-07", "2006-12-05", "2006-02-05", "2006-30-12", "2006-07-04", "2006-28-08", "2006-20-02", "2006-23-11", "2006-20-10", "2006-25-09", ]
df_3["Exam_Date"] = pd.to_datetime(df_3["Exam_Date"], format = "%Y-%d-%m")
print(df_3)
print(df_3["Exam_Date"].dtype)
print(df_3["Exam_Date"].dt.day)          # Day
print(df_3["Exam_Date"].dt.month)        # Month
print(df_3["Exam_Date"].dt.year)         # Year
print(df_3["Exam_Date"].dt.day_name())     # Days of week
print(df_3["Exam_Date"] + pd.Timedelta(days = 90))     # Adding no. of days

# Handling missing values
import numpy as np
print(df_3.isnull())
df_3.loc[0, "Marks"] = np.nan
print(df_3)
print(df_3.fillna(85, inplace = True))
print(df_3)

# Aggregation and group by
df_3["Exam_Month"] = df_3["Exam_Date"].dt.month
print(df_3["Exam_Month"].value_counts())    # Count of all months
print(df_3)
print(df_3[df_3["Exam_Month"]==9].value_counts())    # Count of a particular months
print(df_3.groupby("Exam_Month")["Marks"].sum())     # Finding sum on basis of month
print(df_3.groupby("Exam_Month")["Marks"].mean())    # Finding average on basis of month
print(df_3.groupby("Exam_Month").agg({"Marks":"mean", "Name":"count"}))   # Finding average on basis of month

# Concatenate and Merge Dataframe (JOINS)
# Concatenate
data_4 = {"ID" : [16, 20, 14, 41], "Score" : [89, 67, 80, 85]}
df_4 = pd.DataFrame(data_4)
print(pd.concat([df_2, df_4], axis = 0))   # concatenate on basis of row
print(pd.concat([df_2, df_4], axis = 1))   # concatenate on basis of column
# Merge
print(df_2)
print(df_4)
print(pd.merge(df_2, df_4, how="inner", left_on = "Age", right_on = "ID"))    # how = "inner", "outer", "left", "right"
