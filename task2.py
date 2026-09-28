import pandas as pd

df = pd.read_csv("cleaned_student_data.csv")

print("Dataset loaded successfully!")
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDescriptive Statistics:")
print(df.describe())

print("\nSex distribution:")
print(df["sex"].value_counts())

print("\nSchool distribution:")
print(df["school"].value_counts())

print("\nAge distribution:")
print(df["age"].value_counts().sort_index())

print("\nFinal grade (G3) distribution:")
print(df["G3"].value_counts().sort_index())

print("\nAverage G3 by study time:")
print(df.groupby("studytime")["G3"].mean())

print("\nAverage G3 by number of failures:")
print(df.groupby("failures")["G3"].mean())

print("\nAverage G3 by absences:")
print(df.groupby("absences")["G3"].mean())

print("\nCorrelation with final grade (G3):")
print(df.select_dtypes(include="number").corr()["G3"].sort_values(ascending=False))

import matplotlib.pyplot as plt

correlation = df.select_dtypes(include="number").corr()

plt.figure(figsize=(12, 8))
plt.imshow(correlation, cmap="coolwarm", interpolation="nearest")
plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
plt.hist(df["G3"], bins=10, edgecolor="black")

plt.title("Distribution of Final Grades (G3)")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")

plt.show()
plt.figure(figsize=(8, 5))
plt.scatter(df["G1"], df["G3"])

plt.title("G1 vs Final Grade (G3)")
plt.xlabel("G1 - First Grade")
plt.ylabel("G3 - Final Grade")

plt.show()


avg_g3_failures = df.groupby("failures")["G3"].mean()

plt.figure(figsize=(8, 5))
plt.bar(avg_g3_failures.index, avg_g3_failures.values, edgecolor="black")

plt.title("Average Final Grade by Number of Failures")
plt.xlabel("Number of Failures")
plt.ylabel("Average Final Grade (G3)")

plt.show()


plt.figure(figsize=(8, 5))
plt.scatter(df["absences"], df["G3"])

plt.title("Absences vs Final Grade (G3)")
plt.xlabel("Number of Absences")
plt.ylabel("Final Grade (G3)")

plt.show()
