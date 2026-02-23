#Task 2: The Logic of Dependency (Independent vs. Dependent)
# Independent Events
P_heads = 1/2
P_six = 1/6

P_both = P_heads * P_six

print("Probability of Heads AND 6:", P_both)


# Dependent Events (Without Replacement)

P_first_red = 5/10
P_second_red = 4/9

P_both_red = P_first_red * P_second_red

print("Probability both marbles are Red:", P_both_red)


'''
Output:
    Probability of Heads AND 6: 0.08333333333333333
    Probability both marbles are Red: 0.2222222222222222
'''