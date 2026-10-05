import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print(sns.get_dataset_names())

# Basic Plots in Seaborn
# Line plot
fmri = sns.load_dataset("fmri") 
print(fmri)
sns.lineplot(x = "timepoint", y = "signal", hue = "event", data = fmri)
plt.show()
# Scatter plot
sns.scatterplot(x = "timepoint", y = "signal", hue = "subject", data = fmri)
plt.show()
# Bar plot
sns.barplot(x = "timepoint", y = "signal", data = fmri)
plt.show()
# Box plot
sns.boxplot(x = "event", y = "signal", data = fmri)
plt.show()
# Hist plot
sns.histplot(fmri["region"], kde = True)
plt.show()
# Heat map
corr = fmri.corr(numeric_only = True)
sns.heatmap(corr, annot = True, cmap = "coolwarm")
plt.show()
# Pair plot
iris = sns.load_dataset("iris")
print(iris)
sns.pairplot(iris, hue = "species")
plt.show()
# Strip plot
x = ["sun", "mon", "fri", "sat", "tue", "wed", "thu"]
y = [5, 6.7, 4, 6, 2, 4.9, 1.8]
ax = sns.stripplot(x = x, y = y)
ax.set(xlabel = "Days", ylabel = "Amount Spent")
plt.title("Daily Spending (Custom Data)")
plt.show()
# Swarm plot
sns.swarmplot(x = "species", y = "sepal_length", data = iris)
plt.title("Swarm plot of sepal length by species")
plt.show()
# Bar plot
tips = sns.load_dataset("tips")
sns.barplot(x="sex", y="total_bill", data=tips, palette="plasma")
plt.title("Average Total Bill by Gender")
plt.show()
# Count plot
sns.countplot(x="sex", data=tips)
plt.title("Count of Gender in Dataset")
plt.show()
# Box plot
sns.boxplot(x="day", y="total_bill", data=tips, hue="smoker")
plt.title("Total Bill Distribution by Day & Smoking Status")
plt.show()
# Violin plot
sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)
plt.title("Violin Plot of Total Bill by Day and Gender")
plt.show()
# Strip plot with hue
sns.stripplot(x="day", y="total_bill", data=tips,
              jitter=True, hue="smoker", dodge=True)
plt.title("Total Bill Distribution with Smoking Status")
plt.show()

# Categories of Plots in Seaborn

# Relational plots - relation between two plots
tips = sns.load_dataset("tips")
tips.head()
print(tips)
sns.relplot(data = tips, x = "total_bill", y = "tip", hue = "day", col = "time", row = "sex", size = "size", kind = "scatter")
plt.show()
sns.relplot(data = tips, x = "total_bill", y = "tip", kind = "line")
plt.show()

# Categorical plots - splits graphs into categories in form of strips
# Creating a strip plot
sns.stripplot(data = tips, x = "day", y = "total_bill")
plt.show()
# Creating a swarm plot
sns.swarmplot(data = tips, x = "day", y = "total_bill")
plt.show()
# Creating a box plot
sns.boxplot(data = tips, x = "day", y = "total_bill")
plt.show()
# Creating a violin plot
sns.violinplot(data = tips, x= "day", y = "total_bill")
plt.show()
# Creating a bar plot
sns.barplot(data = tips, x = "day", y = "total_bill")
plt.show()
# Creating a count plot
sns.countplot(data = tips, x = "day")
plt.show()

# Distribution Plots - used to visualize how data values are distributed
sns.set_style("whitegrid")
# Create a joint plot
sns.jointplot(data = tips, x = "total_bill", y = "tip")
plt.show()
# Creating a pair plot
sns.pairplot(tips)
plt.show()
# Creating a rug plot
sns.rugplot(tips["total_bill"])
plt.show()

# Regression Plots - used to visualize relationship between two continuous variables along with regression line
# Simple regression plot
sns.lmplot(x = "total_bill", y= "tip", data = tips)
plt.show()
# Regression plot with categories(hue)
sns.lmplot(x = "total_bill", y = "tip", data = tips, hue = "sex", markers = ["o", "v"])
plt.show()
# Customized regression plot
sns.lmplot(x = "total_bill", y = "tip", data = tips, hue = "sex", markers = ["o","v"], scatter_kws = {"s":100}, palette = "plasma")
plt.show()
# Multiple regression plots
sns.lmplot(x ='total_bill', y ='tip', data = tips, 
           col ='sex', row ='time', hue ='smoker')
plt.show()

# Matrix plot - Visualizes matrices
# Creating correlation matrix
corr_matrix = tips.corr(numeric_only = True)
# heatmap
sns.heatmap(corr_matrix, annot = True, cmap = "coolwarm")
plt.title("Correlation Heatmap")
plt.show()
# cluster map
sns.clustermap(corr_matrix, cmap = "coolwarm", annot = True)
plt.show()

# Multi-Plot Grid - plot numtipe graphs together
g = sns.FacetGrid(tips, col = "time", hue = "sex")
g.map(sns.scatterplot, "total_bill", "tip")
plt.show()


