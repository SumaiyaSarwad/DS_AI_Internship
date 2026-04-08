#Task 3: The Magic of Averages (Central Limit Theorem)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

data = np.random.exponential(scale=50000, size=10000)

sample_means = []

for i in range(1000):
    sample = np.random.choice(data, size=30)
    sample_means.append(np.mean(sample))
df_means = pd.DataFrame(sample_means, columns=["Sample Means"])

df_means["Sample Means"].plot(kind="hist", bins=30, density=True)
df_means["Sample Means"].plot(kind="kde")

plt.title("Distribution of Sample Means (Central Limit Theorem)")
plt.xlabel("Sample Mean")
plt.show()
