import pandas as pd
df =pd.read_csv("student_data.csv")
print(df.head())

print("shape of dataset:",df.shape)
print("\n Column names")
print(df.columns)

print("\n Dataset information")
print(df.info())


print("\nMissing values in each column:")
print(df.isnull().sum())


print("\nNumber of duplicate records:")
print(df.duplicated().sum())

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)

print("\nStatistical summary:")
print(df.describe())
print("\nUnique values in categorical columns:")

for col in df.select_dtypes(include="str").columns:
    print(f"\n{col}:")
    print(df[col].unique())

    print("\nHigh absence values:")
    print(df[df["absences"] > 20][["school", "sex", "age", "absences", "G1", "G2", "G3"]])

Q1 = df["absences"].quantile(0.25)
Q3 = df["absences"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("\nAbsences IQR:")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower limit:", lower)
print("Upper limit:", upper)

print("\nNumber of outliers:", 
      ((df["absences"] < lower) | (df["absences"] > upper)).sum())

print("\nRange validation:")

print("Age:", df["age"].min(), "to", df["age"].max())
print("Medu:", df["Medu"].min(), "to", df["Medu"].max())
print("Fedu:", df["Fedu"].min(), "to", df["Fedu"].max())
print("Studytime:", df["studytime"].min(), "to", df["studytime"].max())
print("Failures:", df["failures"].min(), "to", df["failures"].max())
print("G1:", df["G1"].min(), "to", df["G1"].max())
print("G2:", df["G2"].min(), "to", df["G2"].max())
print("G3:", df["G3"].min(), "to", df["G3"].max())

df.to_csv("cleaned_student_data.csv", index=False)

print("\nCleaned dataset saved successfully!")