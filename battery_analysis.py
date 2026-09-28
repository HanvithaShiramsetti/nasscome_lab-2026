import numpy as np

# Task 1: Python Basics

battery_data = [
    {"time": 0, "temperature": 32, "voltage": 400, "current": 20, "charge": 95},
    {"time": 1, "temperature": 35, "voltage": 395, "current": 22, "charge": 88},
    {"time": 2, "temperature": 38, "voltage": 390, "current": 25, "charge": 80},
    {"time": 3, "temperature": 40, "voltage": 385, "current": 28, "charge": 70},
    {"time": 4, "temperature": 42, "voltage": 380, "current": 30, "charge": 60},
    {"time": 5, "temperature": 45, "voltage": 375, "current": 32, "charge": 48}
]

# Display sensor readings
print("Battery Sensor Readings")
for data in battery_data:
    print(data)

# Check high temperature
print("\nTemperature Analysis")
for data in battery_data:
    if data["temperature"] > 40:
        print(f"Time {data['time']} h: High Temperature Alert")
    else:
        print(f"Time {data['time']} h: Temperature Normal")

# Check low battery
print("\nBattery Charge Analysis")
for data in battery_data:
    if data["charge"] < 50:
        print(f"Time {data['time']} h: Low Battery Alert")
    else:
        print(f"Time {data['time']} h: Battery Charge Normal")

# Battery status function
def battery_status(charge):
    if charge > 70:
        return "High"
    elif charge >= 50:
        return "Medium"
    else:
        return "Low"

print("\nBattery Status")
for data in battery_data:
    print(f"Time {data['time']} h: {battery_status(data['charge'])}")


# Task 2: NumPy Analysis

D = np.array([
    [32, 400, 20, 95],
    [35, 395, 22, 88],
    [38, 390, 25, 80],
    [40, 385, 28, 70],
    [42, 380, 30, 60],
    [45, 375, 32, 48]
])

print("\nNumPy Array")
print(D)

# Shape
print("\nShape:", D.shape)

# Average values
print("Average Temperature:", np.mean(D[:, 0]))
print("Average Voltage:", np.mean(D[:, 1]))
print("Average Current:", np.mean(D[:, 2]))
print("Average Charge:", np.mean(D[:, 3]))

# Maximum and minimum temperature
print("\nMaximum Temperature:", np.max(D[:, 0]))
print("Minimum Temperature:", np.min(D[:, 0]))

# Voltage column
voltage = D[:, 1]
print("\nVoltage Column:")
print(voltage)

# High temperature readings
high_temperature = D[D[:, 0] > 40]
print("\nHigh Temperature Readings:")
print(high_temperature)

# Low battery readings
low_battery = D[D[:, 3] < 50]
print("\nLow Battery Readings:")
print(low_battery)


# Task 3: Linear Algebra

A = np.array([
    [2, 1],
    [1, 3]
])

X = np.array([
    [40],
    [25]
])

# Matrix multiplication
Y = A @ X

print("\nTransformed Output Y = AX:")
print(Y)

# Transpose
print("\nTranspose of A:")
print(A.T)

# Determinant
print("\nDeterminant of A:")
print(np.linalg.det(A))

# Inverse
print("\nInverse of A:")
print(np.linalg.inv(A))

# Solve AX = B
B = np.array([100, 120])

solution = np.linalg.solve(A, B)

print("\nSolution of AX = B:")
print("x =", solution[0])
print("y =", solution[1])


# Task 4: Calculus

def discharge_rate(t):
    return -2 - t

rate_at_2 = discharge_rate(2)
rate_at_5 = discharge_rate(5)

print("\nCalculus Analysis")
print("dC/dt at t = 2:", rate_at_2, "%/hour")
print("dC/dt at t = 5:", rate_at_5, "%/hour")


# Final Analysis

initial_charge = D[0, 3]
final_charge = D[-1, 3]

charge_loss = initial_charge - final_charge

print("\nFinal Analysis")
print("Initial Charge:", initial_charge, "%")
print("Final Charge:", final_charge, "%")
print("Total Charge Loss:", charge_loss, "percentage points")

print("\nFinal Decision: MONITOR")
