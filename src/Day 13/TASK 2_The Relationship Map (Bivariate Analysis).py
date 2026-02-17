# TASK 2 — The Relationship Map (Bivariate Analysis)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

data = {
    "SquareFootage": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000, 3500],
    "Price": [120000, 150000, 200000, 250000, 300000,
              350000, 400000, 500000, 650000, 800000],
    "City": ["Mumbai", "Delhi", "Mumbai", "Bangalore",
             "Delhi", "Chennai", "Mumbai", "Delhi",
             "Bangalore", "Chennai"]
}

df = pd.DataFrame(data)

plt.figure()
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("Square Footage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()


plt.figure()
sns.boxplot(x="City", y="Price", data=df)
plt.title("Price Distribution by City")
plt.xlabel("City")
plt.ylabel("Price")
plt.show()

print("Observation:")
print("As SquareFootage increases, Price also increases.")
print("This indicates a positive relationship between house size and price.")
print("SquareFootage is an important feature for predicting Price.")
