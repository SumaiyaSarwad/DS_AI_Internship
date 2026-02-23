#Task 3: The Bayesian Filter (Conditional Probability & Bayes’ Theorem)
P_spam = 0.1
P_ham = 1 - P_spam

P_free_given_spam = 0.9
P_free_given_ham = 0.05

# Total probability of "Free"
P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)

# Bayes Theorem
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("Probability email is Spam given it contains 'Free':", P_spam_given_free)

'''
Output:
    Probability email is Spam given it contains 'Free': 0.6666666666666667
'''