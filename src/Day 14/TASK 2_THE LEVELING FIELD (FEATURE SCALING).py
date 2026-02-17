# TASK 2 — THE LEVELING FIELD (FEATURE SCALING)
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

data = {
    "Age": [22, 25, 47, 52, 46, 56, 48, 30, 34, 29],
    "Salary": [25000, 32000, 120000, 150000, 110000,
               170000, 130000, 45000, 60000, 52000]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

plt.figure()
plt.hist(df["Salary"], bins=5)
plt.title("Original Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.hist(df_standardized["Salary"], bins=5)
plt.title("Standardized Salary Distribution")
plt.xlabel("Standardized Salary")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.hist(df_normalized["Salary"], bins=5)
plt.title("Normalized Salary Distribution")
plt.xlabel("Normalized Salary")
plt.ylabel("Frequency")
plt.show()

print("\nFeature Scaling Completed Successfully!")
