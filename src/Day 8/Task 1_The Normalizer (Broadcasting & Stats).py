#Task 1: The Normalizer (Broadcasting & Stats)
import numpy as np

scores = np.random.randint(50, 101, size=(5, 3))
mean_scores = scores.mean(axis=0)
centered_scores = scores - mean_scores

print("Original Scores:\n", scores)
print("\nMean Scores (per subject):\n", mean_scores)
print("\nCentered Scores:\n", centered_scores)

'''
Output:
    Original Scores:
     [[ 64  79  60]
     [ 94  97  62]
     [ 77  80  63]
     [ 78  97  75]
     [100  94  96]]

    Mean Scores (per subject):
     [82.6 89.4 71.2]

    Centered Scores:
     [[-18.6 -10.4 -11.2]
     [ 11.4   7.6  -9.2]
     [ -5.6  -9.4  -8.2]
     [ -4.6   7.6   3.8]
     [ 17.4   4.6  24.8]]
'''