#Task 1: The Product Catalog (Series Creation & Indexing)
import pandas as pd

products = pd.Series(
    [700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard'])

laptop_price = products['Laptop']
first_two = products.iloc[:2]

print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst Two Products (Positional Slicing):")
print(first_two)


'''
Output:
    Full Series:
    Laptop      700
    Mouse       150
    Keyboard    300
    dtype: int64

    Price of Laptop:
    700

    First Two Products (Positional Slicing):
    Laptop    700
    Mouse     150
    dtype: int64
'''