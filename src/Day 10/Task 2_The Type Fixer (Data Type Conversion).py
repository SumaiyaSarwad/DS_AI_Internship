#Task 2: The Type Fixer (Data Type Conversion)
import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "Price": ["$1200", "$800", "$400", "$300"],  
    "Date": ["2024-01-05", "2024-02-10", "2024-03-15", "2024-04-20"]  
}

df = pd.DataFrame(data)

print("Data types BEFORE conversion:")
print(df.dtypes)

df["Price"] = df["Price"].str.replace("$", "", regex=False)
df["Price"] = df["Price"].astype(float)

df["Date"] = pd.to_datetime(df["Date"])

print("\nData types AFTER conversion:")
print(df.dtypes)
print("\nFinal DataFrame:")
print(df)

'''
Output:
    Data types BEFORE conversion:
    Product    object
    Price      object
    Date       object
    dtype: object

    Data types AFTER conversion:
    Product            object
    Price             float64
    Date       datetime64[ns]
    dtype: object

    Final DataFrame:
       Product   Price       Date
    0   Laptop  1200.0 2024-01-05
    1    Phone   800.0 2024-02-10
    2   Tablet   400.0 2024-03-15
    3  Monitor   300.0 2024-04-20
'''
