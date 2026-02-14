# STEP 1 — Import pandas
import pandas as pd

# STEP 2 — Create messy dataset (added Date + messy City + duplicate row)
data = {
    "CustomerID": [101,102,103,104,105,106,107,107,108,109],
    "Name": ["Amit","Sara","John",None,"Priya","David","Meena","Meena","Ali","Riya"],
    "Age": [25,None,30,22,None,28,35,35,None,26],
    "City": [" Bangalore","Mumbai ","Delhi",None,"Bangalore","Chennai","Mumbai","Mumbai","Delhi"," Bangalore "],
    "OrderAmount": [2500,1800,None,2200,3000,None,1500,1500,2700,None],
    "PaymentMethod": ["UPI","Card","Cash","Card",None,"UPI","Cash","Cash","Card","UPI"],
    "Date": ["2024-01-05","2024-01-10","2024-02-01","2024-02-05","2024-03-01",
             "2024-03-05","2024-03-10","2024-03-10","2024-04-01","2024-04-05"]
}

df = pd.DataFrame(data)

# STEP 3 — Inspect dataset
print("First rows:\n", df.head())
print("\nDataset info:")
print(df.info())

# STEP 4 — Check missing values
print("\nMissing values per column:")
print(df.isna().sum())

# STEP 5 — Fill missing values (statistical approach)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["OrderAmount"] = df["OrderAmount"].fillna(df["OrderAmount"].mean())
df["City"] = df["City"].fillna(df["City"].mode()[0])
df["PaymentMethod"] = df["PaymentMethod"].fillna(df["PaymentMethod"].mode()[0])
df["Name"] = df["Name"].fillna("Unknown")

# STEP 6 — Check data types before conversion
print("\nData types BEFORE conversion:")
print(df.dtypes)

# STEP 7 — Convert data types
df["Age"] = df["Age"].astype(int)
df["Date"] = pd.to_datetime(df["Date"])

print("\nData types AFTER conversion:")
print(df.dtypes)

# -------------------------------------------------
# NEW PART — STRING CLEANING
# -------------------------------------------------

# Strip extra spaces from City names
df["City"] = df["City"].str.strip()

# Convert City names to lowercase
df["City"] = df["City"].str.lower()

print("\nCity column after cleaning:")
print(df["City"])

# -------------------------------------------------
# NEW PART — DUPLICATE HANDLING
# -------------------------------------------------

# Check duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\nShape after removing duplicates:", df.shape)

# FINAL CLEAN DATASET
print("\nFinal cleaned dataset:")
print(df.head())


# STEP 8 — Save Final Cleaned Dataset
df.to_csv("cleaned_customer_dataset.csv", index=False)

print("\nDataset saved successfully!")

'''
Output:
    First rows:
        CustomerID   Name   Age        City  OrderAmount PaymentMethod        Date
    0         101   Amit  25.0   Bangalore       2500.0           UPI  2024-01-05
    1         102   Sara   NaN     Mumbai        1800.0          Card  2024-01-10
    2         103   John  30.0       Delhi          NaN          Cash  2024-02-01
    3         104   None  22.0        None       2200.0          Card  2024-02-05
    4         105  Priya   NaN   Bangalore       3000.0          None  2024-03-01

    Dataset info:
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10 entries, 0 to 9
    Data columns (total 7 columns):
     #   Column         Non-Null Count  Dtype  
    ---  ------         --------------  -----  
     0   CustomerID     10 non-null     int64  
     1   Name           9 non-null      object 
     2   Age            7 non-null      float64
     3   City           9 non-null      object 
     4   OrderAmount    7 non-null      float64
     5   PaymentMethod  9 non-null      object 
     6   Date           10 non-null     object 
    dtypes: float64(2), int64(1), object(4)
    memory usage: 692.0+ bytes
    None

    Missing values per column:
    CustomerID       0
    Name             1
    Age              3
    City             1
    OrderAmount      3
    PaymentMethod    1
    Date             0
    dtype: int64

    Data types BEFORE conversion:
    CustomerID         int64
    Name              object
    Age              float64
    City              object
    OrderAmount      float64
    PaymentMethod     object
    Date              object
    dtype: object

    Data types AFTER conversion:
    CustomerID                int64
    Name                     object
    Age                       int64
    City                     object
    OrderAmount             float64
    PaymentMethod            object
    Date             datetime64[ns]
    dtype: object

    City column after cleaning:
    0    bangalore
    1       mumbai
    2        delhi
    3        delhi
    4    bangalore
    5      chennai
    6       mumbai
    7       mumbai
    8        delhi
    9    bangalore
    Name: City, dtype: object

    Number of duplicate rows:
    1

    Shape after removing duplicates: (9, 7)

    Final cleaned dataset:
       CustomerID     Name  Age       City  OrderAmount PaymentMethod       Date
    0         101     Amit   25  bangalore  2500.000000           UPI 2024-01-05
    1         102     Sara   28     mumbai  1800.000000          Card 2024-01-10
    2         103     John   30      delhi  2171.428571          Cash 2024-02-01
    3         104  Unknown   22      delhi  2200.000000          Card 2024-02-05
    4         105    Priya   28  bangalore  3000.000000          Card 2024-03-01
'''