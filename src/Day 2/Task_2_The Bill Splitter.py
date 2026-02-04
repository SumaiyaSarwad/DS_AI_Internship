#Task 2: The Bill Splitter

TotalBillAmount = float(input("Enter the amount:"))
NumberOfPeople = int(input("Enter the number of people:"))
SharePerPerson = (TotalBillAmount/NumberOfPeople)
print(f"Total Bill: {TotalBillAmount}. Each person pays: {SharePerPerson}")

print(type(SharePerPerson))
print(type(NumberOfPeople))
print(type(TotalBillAmount))


# Output : Enter the amount: 200
#          Enter the number of people: 4
#          Total Bill: 200.0. Each person pays: 50.0

#         <class 'float'>
#         <class 'int'>
#         <class 'float'>
