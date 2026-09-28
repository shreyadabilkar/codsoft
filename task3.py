import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

print("Dataset loaded successfully!")
print(df.head())


average_g3 = df.groupby("failures")["G3"].mean()

plt.figure(figsize=(8, 5))

plt.bar(
    average_g3.index,
    average_g3.values,
    color="skyblue",
    label="Average G3"
)

plt.title("Average Final Grade by Number of Failures")
plt.xlabel("Number of Failures")
plt.ylabel("Average Final Grade (G3)")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.show()



plt.figure(figsize=(8, 5))

plt.plot(
    average_g3.index,
    average_g3.values,
    marker="o",
    color="green",
    linewidth=2,
    label="Average G3"
)

plt.title("Trend of Average Final Grade by Failures")
plt.xlabel("Number of Failures")
plt.ylabel("Average Final Grade (G3)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()




failure_counts = df["failures"].value_counts().sort_index()

plt.figure(figsize=(7, 7))

plt.pie(
    failure_counts.values,
    labels=failure_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Students by Number of Failures")
plt.tight_layout()

plt.show()



plt.figure(figsize=(8, 5))

plt.hist(
    df["G3"],
    bins=10,
    color="orange",
    edgecolor="black"
)

plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.show()


plt.figure(figsize=(8, 5))

plt.scatter(
    df["studytime"],
    df["G3"],
    color="purple",
    alpha=0.6,
    label="Students"
)

plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade (G3)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()


print("\n========== TASK 3 INSIGHTS ==========")

print("1. Students with fewer failures generally have higher average final grades.")

print("2. The line chart shows a downward trend in average final grade as failures increase.")

print("3. The pie chart shows the percentage of students in each failure category.")

print("4. The histogram shows how the final grades are distributed among students.")

print("5. The scatter plot shows the relationship between study time and final grade.")

print("6. These visualizations help us understand student performance and identify patterns in the dataset.")