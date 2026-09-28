# Integrated Student Performance Analysis

## Introduction

This case study is about analyzing the performance of students using their study hours, attendance, assignment marks, previous marks and final marks.

I used Python, Pandas, NumPy, Data Visualization, Linear Algebra and Calculus to understand the student performance.

## 1. Dataset

The given dataset contains 10 students.

| Student | Study Hours | Attendance | Assignment Score | Previous Score | Final Score |
| ------- | ----------: | ---------: | ---------------: | -------------: | ----------: |
| S1      |           2 |         65 |               55 |             58 |          60 |
| S2      |           3 |         70 |               60 |             62 |          64 |
| S3      |           4 |         75 |               65 |             68 |          70 |
| S4      |           5 |         80 |               72 |             70 |          75 |
| S5      |           6 |         85 |               78 |             76 |          82 |
| S6      |           7 |         90 |               85 |             82 |          88 |
| S7      |           8 |         92 |               88 |             86 |          91 |
| S8      |           4 |         78 |               70 |             72 |          74 |
| S9      |           6 |         88 |               80 |             79 |          84 |
| S10     |           9 |         95 |               92 |             90 |          94 |

## 2. Part A: Python Programming

I created the data using a Python dictionary and then used it to create a DataFrame.

```python
students = {
    "Student": ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"],
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 4, 6, 9],
    "Attendance": [65, 70, 75, 80, 85, 90, 92, 78, 88, 95],
    "Assignment_Score": [55, 60, 65, 72, 78, 85, 88, 70, 80, 92],
    "Previous_Score": [58, 62, 68, 70, 76, 82, 86, 72, 79, 90],
    "Final_Score": [60, 64, 70, 75, 82, 88, 91, 74, 84, 94]
}

print(len(students["Student"]))
```

There are **10 students** in the dataset.

To check the column names:

```python
print(students.keys())
```

To check the first five records and last five records, I used Pandas `head()` and `tail()` after creating the DataFrame.

## 3. Part B: Pandas Analysis

First I created the DataFrame.

```python
import pandas as pd

df = pd.DataFrame(students)
print(df)
```

### Average Values

```python
print(df[["Study_Hours", "Attendance", "Assignment_Score",
          "Previous_Score", "Final_Score"]].mean())
```

The average values are:

| Parameter        | Average |
| ---------------- | ------: |
| Study Hours      |     5.4 |
| Attendance       |   81.8% |
| Assignment Score |    74.5 |
| Previous Score   |    74.3 |
| Final Score      |    78.2 |

So, the average final score is **78.2**.

### Highest Final Score

```python
print(df.loc[df["Final_Score"].idxmax()])
```

The highest final score is:

**S10 = 94**

### Lowest Final Score

```python
print(df.loc[df["Final_Score"].idxmin()])
```

The lowest final score is:

**S1 = 60**

### Students with Attendance Above 80%

```python
print(df[df["Attendance"] > 80])
```

The students are:

**S5, S6, S7, S9 and S10**

### Students with Final Score Above 80

```python
print(df[df["Final_Score"] > 80])
```

The students are:

**S5, S6, S7, S9 and S10**

### Statistical Summary

```python
print(df.describe())
```

This gives values such as mean, minimum, maximum and standard deviation.

## 4. Part C: NumPy Analysis

I converted the final scores into a NumPy array.

```python
import numpy as np

final_scores = np.array(df["Final_Score"])

print("Mean:", np.mean(final_scores))
print("Median:", np.median(final_scores))
print("Maximum:", np.max(final_scores))
print("Minimum:", np.min(final_scores))
print("Standard Deviation:", np.std(final_scores))
```

Results:

* Mean = **78.2**
* Median = **78.5**
* Maximum = **94**
* Minimum = **60**
* Standard Deviation = **10.89**

The standard deviation tells us how much the final scores vary from the average score.

In this dataset, the standard deviation is about **10.89**, which means the scores have some variation around the average of 78.2.

## 5. Part D: Data Visualization

I created four graphs to understand the data better.

### 5.1 Study Hours vs Final Score

```python
import matplotlib.pyplot as plt

plt.scatter(df["Study_Hours"], df["Final_Score"])
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")
plt.show()
```

Observation:

Students who study more hours generally have higher final scores.

For example, S1 studied 2 hours and scored 60, while S10 studied 9 hours and scored 94.

### 5.2 Attendance vs Final Score

```python
plt.scatter(df["Attendance"], df["Final_Score"])
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score")
plt.show()
```

Observation:

Students with higher attendance generally have higher final scores.

### 5.3 Distribution of Final Scores

```python
plt.hist(df["Final_Score"], bins=5)
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.title("Distribution of Final Scores")
plt.show()
```

This graph shows how the final scores are distributed among the students.

### 5.4 Student-wise Final Scores

```python
plt.bar(df["Student"], df["Final_Score"])
plt.xlabel("Student")
plt.ylabel("Final Score")
plt.title("Student-wise Final Scores")
plt.show()
```

From the graph:

* Highest score = **S10 with 94**
* Lowest score = **S1 with 60**

## 6. Part E: Linear Algebra

The matrix contains three input variables:

* Study Hours
* Attendance
* Assignment Score

For example:

```text
S1 = [2, 65, 55]
```

I created the complete matrix using NumPy.

```python
X = df[["Study_Hours", "Attendance", "Assignment_Score"]].values

print("Shape:", X.shape)
print("Transpose:")
print(X.T)

print("X transpose X:")
print(X.T @ X)
```

The shape of the matrix is:

```text
(10, 3)
```

This means there are **10 students and 3 input variables**.

The value of `XᵀX` is:

```text
[[  336   4611   4265]
 [ 4611  67792  62026]
 [ 4265  62026  56851]]
```

### Dot Product of Study Hours and Final Score

```python
dot_product = np.dot(df["Study_Hours"], df["Final_Score"])
print(dot_product)
```

Result:

**4449**

### Why is Matrix Representation Useful?

Matrix representation is useful because many students and many variables can be handled together.

For example, instead of calculating study hours, attendance and assignment marks separately for every student, all of them can be stored in one matrix and processed using matrix operations.

## 7. Part F: Calculus - Differentiation

The given function is:

```text
F(x) = 40 + 5x - 0.2x²
```

where `x` represents study hours.

### Derivative

Differentiate the function:

```text
F'(x) = 5 - 0.4x
```

Now find where:

```text
F'(x) = 0
```

So:

```text
5 - 0.4x = 0

0.4x = 5

x = 12.5
```

Therefore, the derivative becomes zero at **12.5 study hours**.

### Interpretation

This means according to the given mathematical model, the predicted score stops increasing at that point.

The dataset itself only contains study hours from 2 to 9, so 12.5 is a result of the given mathematical model rather than an observed value in the data.

## 8. Part G: Calculus - Integration

The learning benefit function is:

```text
L(x) = 5x - 0.2x²
```

We need to calculate:

```text
∫₀⁵ L(x) dx
```

So:

```text
∫(5x - 0.2x²)dx

= 2.5x² - (0.2/3)x³
```

Applying the limits 0 and 5:

```text
= 54.17
```

Therefore, the value of the integral is approximately:

**54.17**

The area under the curve represents the total learning benefit from 0 to 5 study hours according to the given model.

For numerical calculation in Python:

```python
from scipy.integrate import quad

def L(x):
    return 5*x - 0.2*x**2

result, error = quad(L, 0, 5)

print(result)
```

## 9. Part H: Correlation Analysis

I calculated the correlation between different variables and the final score.

```python
print(df.corr(numeric_only=True))
```

The important correlation values are:

| Variable         | Correlation with Final Score |
| ---------------- | ---------------------------: |
| Study Hours      |                       0.9859 |
| Attendance       |                       0.9973 |
| Assignment Score |                       0.9989 |
| Previous Score   |                       0.9936 |

From these values, **Assignment Score has the strongest correlation with Final Score in this dataset**, with a correlation of about **0.9989**.

A correlation close to 1 means there is a strong positive linear relationship.

I also created a heatmap to view the correlation values.

```python
import seaborn as sns

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()
```

## 10. Part I: Simple Prediction Model

The assignment gives the model:

```text
Y = Xβ
```

The coefficient formula is:

```text
β = (XᵀX)⁻¹XᵀY
```

I used NumPy to calculate the coefficients.

```python
X = df[["Study_Hours", "Attendance", "Assignment_Score"]].values
Y = df["Final_Score"].values

X = np.column_stack((np.ones(len(X)), X))

beta = np.linalg.inv(X.T @ X) @ X.T @ Y

print("Coefficients:")
print(beta)
```

The coefficients are approximately:

```text
Intercept = 0.2733
Study Hours = -0.1817
Attendance = 0.3066
Assignment Score = 0.7225
```

In simple words, the coefficients describe how the input variables are related to the final score in this model.

Assignment Score has the largest positive coefficient among the three input variables.

## 11. Final Results

The main results from the complete analysis are:

* Average Final Score = **78.2**
* Highest Final Score = **94 (S10)**
* Lowest Final Score = **60 (S1)**
* Median Final Score = **78.5**
* Standard Deviation = **10.89**
* Study Hours and Final Score have a strong positive relationship.
* Attendance and Final Score also have a strong positive relationship.
* Assignment Score has the strongest correlation with Final Score.
* Matrix representation makes it easier to work with multiple variables.
* The derivative becomes zero at **12.5 study hours**.
* The integration result from 0 to 5 hours is **54.17**.

## 12. Conclusion

In this case study, I analyzed the performance of 10 students using Python, Pandas, NumPy, Data Visualization, Linear Algebra and Calculus. The average final score is 78.2 and S10 got the highest score of 94. The data shows that students with higher study hours and attendance generally have higher final scores. Assignment Score has the strongest correlation with Final Score in this dataset. I also used matrices to analyze multiple input variables together. The calculus part helped me understand the change in predicted performance and the total learning benefit from the given functions. Overall, this case study shows how programming and mathematics can be used together to analyze student performance.
