#Task 3: The Interest Matcher (Set Operations)
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

print("Friend A:",friend_a)
print("Friend B:",friend_b)
print("Common Interest:",friend_a & friend_b)
print("All Interest:",friend_a | friend_b)
print("Unique Interest:",friend_a - friend_b)


#Output: Friend A: {'Python', 'Cooking', 'Movies', 'Hiking'}
#        Friend B: {'Python', 'Hiking', 'Gaming', 'Photography'}
#        Common Interest: {'Python', 'Hiking'}
#        All Interest: {'Gaming', 'Python', 'Movies', 'Photography', 'Hiking', 'Cooking'}
#        Unique Interest: {'Movies', 'Cooking'}
