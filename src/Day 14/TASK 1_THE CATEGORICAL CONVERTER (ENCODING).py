# TASK 1 — THE CATEGORICAL CONVERTER (ENCODING)
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual", "Automatic"],
    "Color": ["Red", "Blue", "Green", "Red", "Blue"]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

le = LabelEncoder()
df["Transmission_Encoded"] = le.fit_transform(df["Transmission"])

df = pd.get_dummies(df, columns=["Color"], drop_first=True)

df = df.drop("Transmission", axis=1)

print("\nDataset After Encoding:")
print(df)

print("\nCategorical Encoding Completed Successfully!")

'''
Output:
    
Original Dataset:
  Transmission  Color
0    Automatic    Red
1       Manual   Blue
2    Automatic  Green
3       Manual    Red
4    Automatic   Blue

Dataset After Encoding:
   Transmission_Encoded  Color_Green  Color_Red
0                     0        False       True
1                     1        False      False
2                     0         True      False
3                     1        False       True
4                     0        False      False

Categorical Encoding Completed Successfully!
'''