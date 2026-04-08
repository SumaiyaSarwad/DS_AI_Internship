#Task 2: The Grade Filter (Boolean Masking & Missing Data)
import pandas as pd

grades=pd.Series([85, None, 92, 45, None, 78, 55])

missing_series=grades.isnull()
filled_series=grades.fillna(0)
filtered_results = filled_series[filled_series > 60]

print(grades)
print(missing_series)
print(filled_series)
print(filtered_results)

'''
Output:
    0    85.0
    1     NaN
    2    92.0
    3    45.0
    4     NaN
    5    78.0
    6    55.0
    dtype: float64
    0    False
    1     True
    2    False
    3    False
    4     True
    5    False
    6    False
    dtype: bool
    0    85.0
    1     0.0
    2    92.0
    3    45.0
    4     0.0
    5    78.0
    6    55.0
    dtype: float64
    0    85.0
    2    92.0
    5    78.0
    dtype: float64
'''
