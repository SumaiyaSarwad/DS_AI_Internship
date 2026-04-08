#Task 2: The Outlier Detective (Z-Scores)
import numpy as np
import pandas as pd

np.random.seed(42)

data = np.random.normal(loc=50, scale=10, size=100)
data = np.append(data, [120, 130])

df = pd.DataFrame(data, columns=["Values"])

mean = df["Values"].mean()
std = df["Values"].std()

print("Mean (μ):", round(mean, 2))
print("Standard Deviation (σ):", round(std, 2))

df["z_score"] = (df["Values"] - mean) / std
outliers = df[np.abs(df["z_score"]) > 3]

print("\nOutliers Detected:")
print(outliers)

'''
Output:
    Mean (μ): 50.45
    Standard Deviation (σ): 13.91

    Outliers Detected:
         Values   z_score
    100   120.0  4.998558
    101   130.0  5.717283
'''
