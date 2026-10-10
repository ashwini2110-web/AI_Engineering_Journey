import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading dataset
titles = pd.read_csv("Exploratory_Data_Analysis(EDA)_Project_1/netflix_titles.csv")
print(titles)

# Data Inspection
print("=========== Data Inspection ==========")

print("The top 5 data are:")
print(titles.head(5))
print("The last 5 data are:")
print(titles.tail(5))
print("The info if dataset is:")
print(titles.info())
print("The description of dataset is:")
print(titles.describe(include = "all"))
print("The shape of data is:")
print(titles.shape)
print("Columns are:")
print(titles.columns)
print("Missing values are:")
print(titles.duplicated().sum())

# Data Cleaning
print("=========== Data Cleaning ==========")
titles["Director"] = titles["Director"].fillna("Unknown")
titles.drop_duplicates()
titles["Duration"] = pd.to_numeric(titles["Duration"])
# Calculating content age
content_age = 2026
titles["Content_Age"] = content_age - titles["Release_Year"]
print("Cleaned Data is :\n")
print(titles.head())

# Statistical Summary
print("=========== Summary ==========")
print("Movies vs TV Shows")
print(titles["Type"].value_counts())
print("Country Distribution")
print(titles["Country"].value_counts())
print("Genre Distribution")
print(titles["Genre"].value_counts())

# Count Plots
print("=========== Count Plots ==========")

sns.countplot(data = titles, x = "Country", hue = "Country")
plt.title("Country Distribution")
plt.show()

sns.countplot(data = titles, x = "Genre", hue  = "Genre")
plt.title("Genre Distribution")
plt.xticks(rotation = 45)
plt.show()

sns.countplot(data = titles, x="Type", hue="Type")
plt.title("Movies vs TV Shows")
plt.show()

# Histograms
print("=========== Histograms ==========")

sns.histplot(data = titles, x = "Release_Year", kde = True)
plt.title("Content Release Trends")
plt.show()

sns.histplot(data = titles, x = "Duration", kde = True)
plt.title("Duration Distribution")
plt.show()

# Bar Plot
print("=========== Bar Plot ==========")

sns.barplot(data = titles, x = "Genre", y = "Duration", hue = "Genre")
plt.title("Average Duration by Genre")
plt.xticks(rotation = 45)
plt.show()

# Box Plot
print("=========== Box Plot ==========")

sns.boxplot(data = titles, x = "Genre", y = "Duration", hue = "Genre")
plt.title("Average Duration Outliers")
plt.xticks(rotation = 45)
plt.show()

# Violin Plot
print("=========== Violin Plot ==========")

sns.violinplot(data = titles, x = "Genre", y = "Duration", hue = "Genre")
plt.title("Duration Distribution by Genre")
plt.xticks(rotation = 45)
plt.show()

# Pair Plot
print("=========== Pair Plot ==========")

sns.pairplot(data = titles, vars = ["Release_Year", "Duration", "Content_Age"], hue = "Type")
plt.xticks(rotation = 45)
plt.show()

# Heatmap
print("=========== Heatmap ==========")

corr = titles.corr(numeric_only = True)
sns.heatmap(data = corr, annot = True, cmap = "coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Dashboard
print("=========== Dashboard ==========")

plt.figure(figsize = (12,8))

# Country Distribution
plt.subplot(2,2,1)
sns.countplot(data = titles, x = "Country", hue = "Country")
plt.title("Country Distribution")

# Genre Distribution
plt.subplot(2,2,2)
sns.countplot(data = titles, x = "Genre", hue  = "Genre")
plt.title("Genre Distribution")
plt.xticks(rotation = 45)

# Release of Distribution
plt.subplot(2,2,3)
sns.histplot(data = titles, x = "Release_Year", kde = True)
plt.title("Content Release Trends")

# Duration Distribution
plt.subplot(2,2,4)
sns.boxplot(data = titles, y = "Duration")
plt.title("Average Duration Analysis")

plt.tight_layout()
plt.show()

print("\n========== INSIGHTS ==========\n")

print("Most Content Producing Country :")
print(titles["Country"].value_counts().idxmax())

print("Most Popular Genre :")
print(titles["Genre"].value_counts().idxmax())

print("Movie Count :")
print(len(titles[titles["Type"] == "Movie"]))

print("TV Show Count :")
print(len(titles[titles["Type"] == "TV Show"]))

print("Longest Content :")
print(titles.sort_values(by="Duration",ascending=False)[["Title", "Duration"]].head(1))

print("Oldest Content :")
print(titles["Release_Year"].min())

print("Newest Content :")
print(titles["Release_Year"].max())


