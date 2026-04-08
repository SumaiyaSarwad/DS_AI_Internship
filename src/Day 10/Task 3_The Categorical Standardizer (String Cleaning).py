#Task 3: The Categorical Standardizer (String Cleaning)
import pandas as pd

data = {
    "Location": [" New York", "new york", "NEW YORK ", 
                 "Los Angeles", " los angeles ", "LOS ANGELES"]
}

df = pd.DataFrame(data)

print("Unique values BEFORE cleaning:")
print(df["Location"].unique())

df["Location"] = df["Location"].str.strip()
df["Location"] = df["Location"].str.title()

print("\nUnique values AFTER cleaning:")
print(df["Location"].unique())

print("\nFinal cleaned DataFrame:")
print(df)

'''
Output:
    Unique values BEFORE cleaning:
    [' New York' 'new york' 'NEW YORK ' 'Los Angeles' ' los angeles '
     'LOS ANGELES']

    Unique values AFTER cleaning:
    ['New York' 'Los Angeles']

    Final cleaned DataFrame:
          Location
    0     New York
    1     New York
    2     New York
    3  Los Angeles
    4  Los Angeles
    5  Los Angeles
'''