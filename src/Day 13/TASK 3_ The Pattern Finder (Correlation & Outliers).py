# TASK 3 — The Pattern Finder (Correlation & Outliers)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(style="whitegrid")

data = {
    "SquareFootage": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000, 3500],
    "Bedrooms": [1, 2, 2, 3, 3, 4, 4, 4, 5, 5],
    "Price": [120000, 150000, 200000, 250000, 300000,
              350000, 400000, 500000, 650000, 1000000]
}

df = pd.DataFrame(data)

corr_matrix = df.corr(numeric_only=True)

print("Correlation Matrix:\n")
print(corr_matrix)

plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Identify highly correlated features (> 0.8)
print("\nHighly Correlated Feature Pairs (Correlation > 0.8):")

for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.8:
            print(f"{corr_matrix.columns[i]} and {corr_matrix.columns[j]} → {corr_matrix.iloc[i, j]:.2f}")

plt.figure()
sns.boxplot(x=df["Price"])
plt.title("Boxplot of Price (Outlier Detection)")
plt.show()

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["Price"] < lower_bound) | (df["Price"] > upper_bound)]

print("\nOutliers in Price column:")
print(outliers)

print("\nObservations:")
print("1. SquareFootage and Price show very high positive correlation (> 0.8).")
print("2. High correlation may indicate multicollinearity.")
print("3. The boxplot shows a high-value outlier in the Price column.")
print("4. Outliers can impact mean values and ML model performance.")
