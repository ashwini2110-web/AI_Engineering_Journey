import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Retrieving student data
data = pd.read_csv("C:/Users/Ashwini/Documents/GitHub/AI_Engineering_Journey/01_Python/Pandas/16_pandas_project/cleaned_students.csv")
print(data)
# Count plot - How many students belong to each city?
sns.countplot(data = data, x = "City", hue = "City")
plt.title("Students per City")
plt.xlabel("City")
plt.show()

# Bar plot - Which city performs best?
sns.barplot(data = data, x = "City", y = "Percentage", hue = "City")
plt.title("Average Percentage by City")
plt.xlabel("City")
plt.ylabel("Percentage")
plt.show()

# Histogram - How are marks distributed?
sns.histplot(data = data, x = "Percentage", kde = True)
plt.title("Percentage Distribution")
plt.xticks(rotation = 50)
plt.xlabel("Percentage")
plt.ylabel("Count")
plt.show()

# Scatter plot
sns.scatterplot(data = data, x = "Attendance",y = "Percentage", hue = "Grade")
plt.title("Attendance vs Percentage")
plt.xlabel("Attendance")
plt.ylabel("Percentage")
plt.show()

# Box plot - Are there outliers
sns.boxplot(data = data, x = "Grade", y = "Percentage")
plt.title("Percentage by Grade")
plt.xlabel("Grade")
plt.ylabel("Percentage")
plt.show()

# Violin plot - What is the performance distribution in each city?
sns.violinplot(data = data, x = "City", y = "Percentage")
plt.title("Percentage by City")
plt.xlabel("City")
plt.ylabel("Percentage")
plt.show()

# Heat map - Which numeric variables are strongly related?
corr = data.corr(numeric_only = True)
plt.figure(figsize = (10,8))
sns.heatmap(corr , annot = True, cmap = "coolwarm")
plt.title("HeatMap")
plt.show()

# Pair plot - How do subjects relate to each other?
sns.pairplot(data = data, vars = ["Math", "Science", "English", "Percentage"], hue = "Grade")
plt.show()


