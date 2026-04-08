# TASK 1 — The Distribution Deep-Dive (Univariate Analysis)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

sns.set(style="whitegrid")

data = {
    "Price": [120000, 150000, 200000, 250000, 300000,
              180000, 220000, 275000, 500000, 750000,
              900000, 1000000],
    "City": ["Mumbai", "Delhi", "Mumbai", "Bangalore",
             "Delhi", "Chennai", "Mumbai", "Delhi",
             "Bangalore", "Mumbai", "Delhi", "Chennai"]
}

df = pd.DataFrame(data)

plt.figure()
sns.histplot(df["Price"], kde=True)
plt.title("Histogram of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

price_skew = skew(df["Price"])
price_kurt = kurtosis(df["Price"])

print("Skewness:", price_skew)
print("Kurtosis:", price_kurt)

if price_skew > 0:
    print("Interpretation: Price distribution is Right-Skewed.")
elif price_skew < 0:
    print("Interpretation: Price distribution is Left-Skewed.")
else:
    print("Interpretation: Price distribution is Approximately Normal.")

plt.figure()
sns.countplot(x="City", data=df)
plt.title("Count Plot of Cities")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()

most_frequent_city = df["City"].mode()[0]
print("Most Frequent City (Mode):", most_frequent_city)

print("\nConclusion:")
print("1. Housing prices are positively skewed due to high-value properties.")
print("2. Log transformation may help normalize the data before ML modeling.")
print("3. The most frequent city in the dataset is:", most_frequent_city)
