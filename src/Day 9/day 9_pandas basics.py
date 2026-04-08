#Introduction to pandas 
import pandas as pd

s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print(s1)
print(s2)

'''
Output:
    0    10
    1    20
    2    30
    3    40
    dtype: int64
    a    10
    b    20
    c    30
    dtype: int64
'''
#################################################################################
#Indexing and Selection 
marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])

print(marks['Math'])
print(marks[['Math', 'Chemistry']])

'''
Output:
    85
    Math         85
    Chemistry    78
    dtype: int64
'''
##################################################################################
#Boolean Masking in Series
scores = pd.Series([45, 67, 89, 34, 90])

passed = scores[scores > 60]
print(passed)

'''
Output:
    1    67
    2    89
    4    90
    dtype: int64
'''
###############################################################################
#Handling Missing data in series
data = pd.Series([10, None, 30, None])

print(data.isnull())
print(data.fillna(0))

'''
Output:
    0    False
    1     True
    2    False
    3     True
    dtype: bool
    0    10.0
    1     0.0
    2    30.0
    3     0.0
    dtype: float64
'''
##################################################################################
#Vectorized String Operations
names = pd.Series(['Alice', 'bob', 'CHARLIE'])

print(names.str.lower())
print(names.str.upper())
print(names.str.contains('a'))

'''
Output:
    0      alice
    1        bob
    2    charlie
    dtype: object
    0      ALICE
    1        BOB
    2    CHARLIE
    dtype: object
    0    False
    1    False
    2    False
    dtype: bool
'''
