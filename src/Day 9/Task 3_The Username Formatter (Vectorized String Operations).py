#Task 3: The Username Formatter (Vectorized String Operations)
import pandas as pd

usernames=pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

removed_whitespaces=usernames.str.strip()
lowercase =removed_whitespaces.str.lower()
contains_a =lowercase.str.contains('a')

print(removed_whitespaces)
print(lowercase)
print(contains_a)

'''
Output:
   0           Alice
   1             bOB
   2    Charlie_Data
   3           daisy
   dtype: object
   0           alice
   1             bob
   2    charlie_data
   3           daisy
   dtype: object
   0     True
   1    False
   2     True
   3     True
   dtype: bool
'''