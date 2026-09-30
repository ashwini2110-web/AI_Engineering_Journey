import matplotlib.pyplot as plt

# Create first chart
x_1 = [1,2,3,4,5]
y_1 = [10,20,25,35,45]
chart_1 = plt.plot(x_1,y_1)
# plt.show()           # To display chart

# Customize Chart
plt.figure(figsize = (4,2))     # Figure size
plt.plot(x_1, y_1, color = "green", marker = "o", linestyle = "dashed", linewidth = 2, markersize = 12)
plt.title("First Line Chart on Matplotlib")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Advanced line chart - Multiple lines and legends
x_2 = [10,20,30,40,50]
y1_2 = [12,25,38,41,59]
y2_2 = [15,20,51,68,70]
plt.figure(figsize = (4,2))
plt.plot(x_2, y1_2, label = "Sales of 2024", color = "blue", marker = "o")
plt.plot(x_2, y2_2, label = "Sales of 2025", color = "red", marker = "o")
plt.title("Sales of two years")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()

# Bar Chart
x = ["A","B","C","D","E"]
y = [10,20,25,55,45]
plt.figure(figsize = (4,2))
plt.bar(x,y)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

# Histogram Chart
import random
data = [random.randint(1,10) for _ in range(100)]
plt.figure(figsize = (4,2))
plt.hist(data, bins = 10)     
plt.title("Histogram Chart")

# Pie Chart
categories = ["A","B","C","D","E"]
sales = [10,20,25,55,45]
plt.figure(figsize = (6,4))
plt.pie(sales, labels = categories, autopct = "%1.1f%%", startangle = 90)
plt.title("Pie Chart")

# Scatter Plot - Used to find relationship between variables
y1_2 = [12,25,38,41,59]
y2_2 = [15,20,51,68,70]
plt.figure(figsize = (6,4))
plt.scatter(y1_2, y2_2)
plt.title("Relationship Between Two Variables")
plt.xlabel("Variable 1")
plt.ylabel("Variable 2")

# Subplots
# data_1 = Bar chart
days = ["Mon","Tue","Wed","Thu","Fri"]
sales = [10,20,25,55,45]
# data_2 = Scatter plot
y1_2 = [12,25,38,41,59]
y2_2 = [15,20,51,68,70]
plt.figure(figsize = (7,5))
# first plot - bar chart
plt.subplot(1,2,1)        # row, column, position
plt.bar(days, sales)
plt.title("Weekly Sales")
plt.xlabel("Week Days")
plt.ylabel("Sales")
# second plot - scatter chart
plt.subplot(1,2,2)        # row, column, position
plt.scatter(y1_2, y2_2)
plt.title("User Example")
plt.xlabel("User 1")
plt.ylabel("User 2")
plt.show()