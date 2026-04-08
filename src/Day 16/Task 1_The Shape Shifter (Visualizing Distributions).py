#Task 1: The Shape Shifter (Visualizing Distributions)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

heights = np.random.normal(loc=165, scale=7, size=1000)
income = np.random.exponential(scale=50000, size=1000)
scores = 100 - np.random.exponential(scale=15, size=1000)

def analyze_data(data, title):
    df = pd.DataFrame(data, columns=["Values"])
    
    mean = df["Values"].mean()
    median = df["Values"].median()
    
    print(f"\n{title}")
    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    
    if mean > median:
        print("Right-Skewed Distribution")
    elif mean < median:
        print("Left-Skewed Distribution")
    else:
        print("Normal Distribution")
    
    df["Values"].plot(kind="hist", bins=30, density=True)
    df["Values"].plot(kind="kde")
    plt.title(title)
    plt.show()

analyze_data(heights, "Human Heights (Normal)")
analyze_data(income, "Household Income (Right-Skewed)")
analyze_data(scores, "Easy Exam Scores (Left-Skewed)")

'''
Output:
    Human Heights (Normal)
    Mean: 165.14
    Median: 165.18
    Left-Skewed Distribution
    
    Household Income (Right-Skewed)
    Mean: 50399.3
    Median: 36296.56
    Right-Skewed Distribution
    
    Easy Exam Scores (Left-Skewed)
    Mean: 85.4
    Median: 89.85
    Left-Skewed Distribution
'''
