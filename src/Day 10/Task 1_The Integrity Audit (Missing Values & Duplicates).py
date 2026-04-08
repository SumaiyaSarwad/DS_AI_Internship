#Task 1: The Integrity Audit (Missing Values & Duplicates)
import pandas as pd

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

print("Shape BEFORE cleaning:", df.shape)
print("\nMissing values per column:")
print(df.isna().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())
df["OrderAmount"] = df["OrderAmount"].fillna(df["OrderAmount"].median())
df["City"] = df["City"].fillna(df["City"].mode()[0])
df["PaymentMethod"] = df["PaymentMethod"].fillna(df["PaymentMethod"].mode()[0])
df["Name"] = df["Name"].fillna("Unknown")

df["Age"] = df["Age"].astype(int)
df["Date"] = pd.to_datetime(df["Date"])

df["City"] = df["City"].str.strip().str.lower()

print("\nNumber of duplicate rows BEFORE removal:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nShape AFTER cleaning:", df.shape)
print("\nFinal cleaned dataset:")
print(df.head())

'''
Output:
    Shape BEFORE cleaning: (10, 7)

    Missing values per column:
    CustomerID       0
    Name             1
    Age              3
    City             1
    OrderAmount      3
    PaymentMethod    1
    Date             0
    dtype: int64

    Number of duplicate rows BEFORE removal:
    1

    Shape AFTER cleaning: (9, 7)

    Final cleaned dataset:
       CustomerID     Name  Age       City  OrderAmount PaymentMethod       Date
    0         101     Amit   25  bangalore       2500.0           UPI 2024-01-05
    1         102     Sara   28     mumbai       1800.0          Card 2024-01-10
    2         103     John   30      delhi       2200.0          Cash 2024-02-01
    3         104  Unknown   22      delhi       2200.0          Card 2024-02-05
    4         105    Priya   28  bangalore       3000.0          Card 2024-03-01
'''
