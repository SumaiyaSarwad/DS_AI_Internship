# Probability of rolling a 4 on a fair die
favorable = 1
total_outcomes = 6
probability = favorable / total_outcomes
print(probability)

'''
Output:
    0.16666666666666666
'''

# Independent events example
p_rain = 0.3
p_traffic = 0.2
p_both = p_rain * p_traffic
print(p_both)

'''
Output:
    0.06
'''

# Conditional probability example
p_A_and_B = 0.1
p_B = 0.4
p_A_given_B = p_A_and_B / p_B
print(p_A_given_B)

'''
Output:
    0.25
'''

# Bayes' theorem example
p_disease = 0.01
p_positive_given_disease = 0.9
p_positive = 0.05

p_disease_given_positive = (p_positive_given_disease * p_disease) / p_positive
print(p_disease_given_positive)

'''
Output:
    0.18000000000000002
'''
    
    