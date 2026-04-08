#Task 1: The Sample Space Map (Fundamentals)
import random

actions = ["Click", "Scroll", "Exit"]

sample_space = []

for first in actions:
    for second in actions:
        sample_space.append((first, second))

print("Sample Space:", sample_space)
print("Total outcomes:", len(sample_space))

# Event: Customer clicks at least once
count = 0

for outcome in sample_space:
    if "Click" in outcome:
        count += 1

probability = count / len(sample_space)

print("Probability of at least one Click:", probability)

trials = 1000
count_sum_7 = 0

for _ in range(trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    if dice1 + dice2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("Number of times sum was 7:", count_sum_7)
print("Experimental Probability:", experimental_probability)

'''
Output:
    Sample Space: [('Click', 'Click'), ('Click', 'Scroll'), ('Click', 'Exit'), ('Scroll', 'Click'), ('Scroll', 'Scroll'), ('Scroll', 'Exit'), ('Exit', 'Click'), ('Exit', 'Scroll'), ('Exit', 'Exit')]
    Total outcomes: 9
    Probability of at least one Click: 0.5555555555555556
    Number of times sum was 7: 170
    Experimental Probability: 0.17
'''
