# Smart Electric Vehicle Battery Performance Analysis

## Introduction

This case study is about analyzing the performance of an Electric Vehicle (EV) battery using sensor data collected during a 6-hour test.

The given data contains:

* Temperature
* Voltage
* Current
* Battery Charge

In this case study, I used Python, NumPy, Linear Algebra and Calculus to analyze the battery data and check its condition.

## 1. Given Battery Data

The battery readings given in the problem are:

| Time (h) | Temperature (°C) | Voltage (V) | Current (A) | Charge (%) |
| -------- | ---------------: | ----------: | ----------: | ---------: |
| 0        |               32 |         400 |          20 |         95 |
| 1        |               35 |         395 |          22 |         88 |
| 2        |               38 |         390 |          25 |         80 |
| 3        |               40 |         385 |          28 |         70 |
| 4        |               42 |         380 |          30 |         60 |
| 5        |               45 |         375 |          32 |         48 |

From the data, we can see that the temperature and current are increasing, while the voltage and battery charge are decreasing.

# 2. Task 1: Python Basics

## 2.1 Storing the Data

I stored the battery readings using a list of dictionaries.

```python
battery_data = [
    {"time": 0, "temperature": 32, "voltage": 400, "current": 20, "charge": 95},
    {"time": 1, "temperature": 35, "voltage": 395, "current": 22, "charge": 88},
    {"time": 2, "temperature": 38, "voltage": 390, "current": 25, "charge": 80},
    {"time": 3, "temperature": 40, "voltage": 385, "current": 28, "charge": 70},
    {"time": 4, "temperature": 42, "voltage": 380, "current": 30, "charge": 60},
    {"time": 5, "temperature": 45, "voltage": 375, "current": 32, "charge": 48}
]
```

## 2.2 Displaying the Readings

I used a `for` loop to display all the readings.

```python
for data in battery_data:
    print(data)
```

This prints all the battery readings one by one.

## 2.3 Checking High Temperature

The given condition is:

```text
If temperature > 40°C
High Temperature Alert
```

Python code:

```python
for data in battery_data:
    if data["temperature"] > 40:
        print("High Temperature Alert")
    else:
        print("Temperature Normal")
```

From the data, temperature becomes greater than 40°C at:

```text
Time = 4 hours
Temperature = 42°C
```

At 5 hours, it becomes 45°C.

So, the first high-temperature condition occurs at **4 hours**.

## 2.4 Checking Low Battery

The condition given is:

```text
If charge < 50%
Low Battery Alert
```

Python code:

```python
for data in battery_data:
    if data["charge"] < 50:
        print("Low Battery Alert")
    else:
        print("Battery Charge Normal")
```

At 5 hours:

```text
Charge = 48%
```

Therefore, the low battery alert occurs at **5 hours**.

## 2.5 Battery Status Function

The assignment asks to create a function called `battery_status(charge)`.

The conditions are:

* Charge > 70: High
* Charge between 50 and 70: Medium
* Charge < 50: Low

```python
def battery_status(charge):
    if charge > 70:
        return "High"
    elif charge >= 50:
        return "Medium"
    else:
        return "Low"
```

Example:

```python
print(battery_status(95))
print(battery_status(60))
print(battery_status(48))
```

Output:

```text
High
Medium
Low
```

So the function correctly classifies the battery charge.

# 3. Task 2: NumPy Analysis

## 3.1 Creating the NumPy Array

First, I imported NumPy.

```python
import numpy as np
```

Then I created the battery data as a NumPy array.

```python
D = np.array([
    [32, 400, 20, 95],
    [35, 395, 22, 88],
    [38, 390, 25, 80],
    [40, 385, 28, 70],
    [42, 380, 30, 60],
    [45, 375, 32, 48]
])
```

The columns are:

```text
Temperature, Voltage, Current, Charge
```

## 3.2 Finding the Shape

```python
print(D.shape)
```

Output:

```text
(6, 4)
```

Therefore:

* Rows = 6
* Columns = 4

There are 6 sensor readings and 4 parameters.

## 3.3 Average Temperature

```python
print(np.mean(D[:, 0]))
```

Calculation:

```text
(32 + 35 + 38 + 40 + 42 + 45) / 6
= 232 / 6
= 38.67°C
```

Average temperature = **38.67°C**

## 3.4 Average Voltage

```python
print(np.mean(D[:, 1]))
```

Calculation:

```text
(400 + 395 + 390 + 385 + 380 + 375) / 6
= 2325 / 6
= 387.5 V
```

Average voltage = **387.5 V**

## 3.5 Average Current

```python
print(np.mean(D[:, 2]))
```

Calculation:

```text
(20 + 22 + 25 + 28 + 30 + 32) / 6
= 157 / 6
= 26.17 A
```

Average current = **26.17 A**

## 3.6 Average Battery Charge

```python
print(np.mean(D[:, 3]))
```

Calculation:

```text
(95 + 88 + 80 + 70 + 60 + 48) / 6
= 441 / 6
= 73.5%
```

Average battery charge = **73.5%**

## 3.7 Average Values

| Parameter   | Average |
| ----------- | ------: |
| Temperature | 38.67°C |
| Voltage     | 387.5 V |
| Current     | 26.17 A |
| Charge      |   73.5% |

## 3.8 Maximum and Minimum Temperature

```python
maximum_temperature = np.max(D[:, 0])
minimum_temperature = np.min(D[:, 0])

print("Maximum Temperature:", maximum_temperature)
print("Minimum Temperature:", minimum_temperature)
```

Output:

```text
Maximum Temperature: 45
Minimum Temperature: 32
```

So:

* Maximum temperature = **45°C**
* Minimum temperature = **32°C**

## 3.9 Extracting the Voltage Column

The voltage is in column index 1.

```python
voltage = D[:, 1]
print(voltage)
```

Output:

```text
[400 395 390 385 380 375]
```

The voltage is decreasing with time.

## 3.10 Finding High Temperature Readings

Condition:

```text
Temperature > 40°C
```

Code:

```python
high_temperature = D[D[:, 0] > 40]
print(high_temperature)
```

Output:

```text
[[42 380 30 60]
 [45 375 32 48]]
```

So the high-temperature readings are:

* 42°C at 4 hours
* 45°C at 5 hours

## 3.11 Finding Low Battery Readings

Condition:

```text
Charge < 50%
```

Code:

```python
low_battery = D[D[:, 3] < 50]
print(low_battery)
```

Output:

```text
[[45 375 32 48]]
```

Therefore, the low battery reading occurs at:

```text
Time = 5 hours
Charge = 48%
```

# 4. Task 3: Linear Algebra

The given matrix is:

```text
A = [ 2  1 ]
    [ 1  3 ]
```

The input vector is:

```text
X = [ 40 ]
    [ 25 ]
```

We need to calculate:

```text
Y = AX
```

## 4.1 Matrix Multiplication

Python code:

```python
A = np.array([
    [2, 1],
    [1, 3]
])

X = np.array([
    [40],
    [25]
])

Y = A @ X

print(Y)
```

Calculation:

```text
Y = [2  1] [40]
    [1  3] [25]
```

First value:

```text
2(40) + 1(25)
= 80 + 25
= 105
```

Second value:

```text
1(40) + 3(25)
= 40 + 75
= 115
```

Therefore:

```text
Y = [105]
    [115]
```

So the output vector is **[105, 115]**.

## 4.2 Transpose of A

```python
print(A.T)
```

Output:

```text
[[2 1]
 [1 3]]
```

So:

```text
Aᵀ = [2 1]
     [1 3]
```

The transpose is the same as A in this case.

## 4.3 Determinant of A

For a 2 × 2 matrix:

```text
det(A) = ad - bc
```

Therefore:

```text
det(A)
= (2 × 3) - (1 × 1)
= 6 - 1
= 5
```

Using NumPy:

```python
print(np.linalg.det(A))
```

The determinant is **5**.

Since the determinant is not zero, the inverse exists.

## 4.4 Inverse of A

```python
print(np.linalg.inv(A))
```

The inverse is:

```text
A⁻¹ = [ 0.6  -0.2 ]
      [ -0.2  0.4 ]
```

## 4.5 Solving the Equations

The equations given are:

```text
2x + y = 100

x + 3y = 120
```

Matrix form:

```text
AX = B
```

where:

```text
A = [2 1]
    [1 3]

B = [100]
    [120]
```

Using NumPy:

```python
A = np.array([
    [2, 1],
    [1, 3]
])

B = np.array([100, 120])

answer = np.linalg.solve(A, B)

print(answer)
```

Output:

```text
[36. 28.]
```

Therefore:

```text
x = 36
y = 28
```

Checking:

```text
2(36) + 28 = 100

36 + 3(28) = 120
```

Both equations are satisfied.

# 5. Task 4: Calculus

The battery charge function given in the assignment is:

```text
C(t) = 100 - 2t - 1/2 t²
```

where:

* C(t) = battery charge
* t = time in hours

## 5.1 Finding the Rate of Change

We need to find:

```text
dC/dt
```

Given:

```text
C(t) = 100 - 2t - 1/2 t²
```

Differentiating:

```text
dC/dt = -2 - t
```

The negative value means that the battery charge is decreasing.

## 5.2 Discharge Rate at t = 2

```text
dC/dt = -2 - t
```

At t = 2:

```text
dC/dt = -2 - 2
       = -4 %/hour
```

So at 2 hours, the battery is losing charge at a rate of **4% per hour**.

## 5.3 Discharge Rate at t = 5

At t = 5:

```text
dC/dt = -2 - 5
       = -7 %/hour
```

So at 5 hours, the battery is losing charge at a rate of **7% per hour**.

## 5.4 Interpretation

At 2 hours:

```text
-4 %/hour
```

At 5 hours:

```text
-7 %/hour
```

The magnitude of the discharge rate is increasing.

Therefore, according to the mathematical model, the battery is losing charge at an **increasing rate**.

# 6. Final Analysis

## 6.1 Safety

The first time the temperature exceeds 40°C is:

```text
Time = 4 hours
Temperature = 42°C
```

At 5 hours, the temperature reaches 45°C.

Therefore, temperature needs to be monitored.

## 6.2 Total Charge Reduction

Initial charge:

```text
95%
```

Final charge:

```text
48%
```

Therefore:

```text
Charge Loss = 95 - 48
            = 47%
```

The battery charge reduced by **47 percentage points** during the test.

## 6.3 Important Results

| Parameter             |               Result |
| --------------------- | -------------------: |
| Average Temperature   |              38.67°C |
| Average Voltage       |              387.5 V |
| Average Current       |              26.17 A |
| Average Charge        |                73.5% |
| Maximum Temperature   |                 45°C |
| Minimum Temperature   |                 32°C |
| Charge Loss           | 47 percentage points |
| Discharge Rate at 2 h |             -4%/hour |
| Discharge Rate at 5 h |             -7%/hour |

# 7. Final Decision

## MONITOR

Based on the given data, I selected **MONITOR**.

The main reasons are:

1. Temperature goes above 40°C and reaches 45°C.
2. Battery charge falls below 50% at 5 hours.
3. Voltage continuously decreases.
4. Current continuously increases.
5. The calculated discharge rate increases in magnitude from 4%/hour to 7%/hour.

So, the battery should be continuously monitored during operation.

# 8. Factors That May Make the Battery Unsafe

From the given data, the following factors need attention.

### Increasing Temperature

Temperature increases from 32°C to 45°C.

### Increasing Current

Current increases from 20 A to 32 A.

### Decreasing Voltage

Voltage decreases from 400 V to 375 V.

### Decreasing Battery Charge

Charge decreases from 95% to 48%.

### Increasing Discharge Rate

The discharge rate changes from -4%/hour at 2 hours to -7%/hour at 5 hours.

These values show that the battery condition is changing during the test.

# 9. Additional Data I Would Collect

To analyze the battery more accurately, I would collect:

* Individual cell temperature
* Individual cell voltage
* Battery State of Health (SOH)
* Battery State of Charge (SOC)
* Internal resistance
* Charging and discharging cycles
* Ambient temperature
* Cooling system information
* Battery fault or error information

For example, individual cell temperature can help identify if one particular cell is becoming hotter than the others.

Similarly, individual cell voltage can help identify voltage imbalance between cells.

# 10. Conclusion

In this case study, I analyzed EV battery sensor data using Python, NumPy, Linear Algebra and Calculus.

Using Python, I stored the data and checked high temperature and low battery conditions.

Using NumPy, I calculated the shape, averages, maximum and minimum temperature, voltage column and filtered high-temperature and low-battery readings.

Using Linear Algebra, I calculated the matrix multiplication, transpose, determinant, inverse and solved the given system of equations.

Using Calculus, I found the rate of change of battery charge and calculated the discharge rate at 2 hours and 5 hours.

From the overall analysis, temperature is increasing, voltage is decreasing, current is increasing and battery charge is decreasing. The mathematical model also shows that the discharge rate is increasing.

Therefore, my final decision is:

**MONITOR — The battery requires continuous monitoring.**
