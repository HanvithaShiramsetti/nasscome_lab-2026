import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create the data
data = {
    "Student": ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"],
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 4, 6, 9],
    "Attendance": [65, 70, 75, 80, 85, 90, 92, 78, 88, 95],
    "Assignment_Score": [55, 60, 65, 72, 78, 85, 88, 70, 80, 92],
    "Previous_Score": [58, 62, 68, 70, 76, 82, 86, 72, 79, 90],
    "Final_Score": [60, 64, 70, 75, 82, 88, 91, 74, 84, 94]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student Data:")
print(df)

# Basic information
print("\nNumber of students:", len(df))
print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nFirst 5 students:")
print(df.head())

print("\nLast 5 students:")
print(df.tail())


# Pandas Analysis
print("\nAverage Values:")
print("Study Hours:", df["Study_Hours"].mean())
print("Attendance:", df["Attendance"].mean())
print("Assignment Score:", df["Assignment_Score"].mean())
print("Previous Score:", df["Previous_Score"].mean())
print("Final Score:", df["Final_Score"].mean())

print("\nHighest Final Score:")
print(df.loc[df["Final_Score"].idxmax()])

print("\nLowest Final Score:")
print(df.loc[df["Final_Score"].idxmin()])

print("\nStudents with attendance above 80:")
print(df[df["Attendance"] > 80])

print("\nStudents with final score above 80:")
print(df[df["Final_Score"] > 80])

print("\nStatistical Summary:")
print(df.describe())


# NumPy
final_scores = np.array(df["Final_Score"])

print("\nNumPy Analysis")
print("Mean:", np.mean(final_scores))
print("Median:", np.median(final_scores))
print("Maximum:", np.max(final_scores))
print("Minimum:", np.min(final_scores))
print("Standard Deviation:", np.std(final_scores))


# Graph 1: Study Hours vs Final Score
plt.scatter(df["Study_Hours"], df["Final_Score"])
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")
plt.savefig("study_hours_vs_final.png")
plt.show()


# Graph 2: Attendance vs Final Score
plt.scatter(df["Attendance"], df["Final_Score"])
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score")
plt.savefig("attendance_vs_final.png")
plt.show()


# Graph 3: Final Score Histogram
plt.hist(df["Final_Score"], bins=5)
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.title("Distribution of Final Scores")
plt.savefig("final_score_histogram.png")
plt.show()


# Graph 4: Student-wise Final Score
plt.bar(df["Student"], df["Final_Score"])
plt.xlabel("Student")
plt.ylabel("Final Score")
plt.title("Student-wise Final Scores")
plt.savefig("student_final_scores.png")
plt.show()


# Linear Algebra
X = df[["Study_Hours", "Attendance", "Assignment_Score"]].values

print("\nLinear Algebra")
print("Shape of X:", X.shape)

print("\nTranspose of X:")
print(X.T)

print("\nX transpose X:")
print(X.T @ X)

dot_product = np.dot(df["Study_Hours"], df["Final_Score"])
print("\nDot Product of Study Hours and Final Score:", dot_product)


# Differentiation
# F(x) = 40 + 5x - 0.2x^2
print("\nCalculus - Differentiation")

for x in [2, 4, 6, 8]:
    F = 40 + 5*x - 0.2*x**2
    dF = 5 - 0.4*x
    print("x =", x, "F(x) =", F, "F'(x) =", dF)

x = 5 / 0.4
print("F'(x) = 0 when x =", x)


# Integration
# L(x) = 5x - 0.2x^2

x_values = np.linspace(0, 5, 100)
y_values = 5*x_values - 0.2*x_values**2

area = np.trapezoid(y_values, x_values)

print("\nIntegration")
print("Area from 0 to 5 =", area)


# Correlation
correlation = df.corr(numeric_only=True)

print("\nCorrelation Matrix:")
print(correlation)

print("\nCorrelation with Final Score:")
print(correlation["Final_Score"])

# Heatmap
sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()


# Simple Prediction Model
X = df[["Study_Hours", "Attendance", "Assignment_Score"]].values
Y = df["Final_Score"].values

X = np.column_stack((np.ones(len(X)), X))

beta = np.linalg.inv(X.T @ X) @ X.T @ Y

print("\nPrediction Model Coefficients:")
print("Intercept:", beta[0])
print("Study Hours:", beta[1])
print("Attendance:", beta[2])
print("Assignment Score:", beta[3])


# Final Results
print("\nFinal Results")
print("Average Final Score:", df["Final_Score"].mean())
print("Highest Score:", df["Final_Score"].max())
print("Lowest Score:", df["Final_Score"].min())
print("Median:", np.median(final_scores))
print("Standard Deviation:", np.std(final_scores))

print("\nAnalysis completed.")
