Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a={"key":"Value"}
print(a)
{'key': 'Value'}
b={"Numbers":2}
print(b)
{'Numbers': 2}
###############################################################
#Dictionary
student={
    "name":"Amit",
    "age":21,
    "course":"Engineering"}
print(student["name"])
Amit
student["age"]=22
student["city"]="Delhi"
print(student)
{'name': 'Amit', 'age': 22, 'course': 'Engineering', 'city': 'Delhi'}
##############################################################
#Dictionary Methods
marks={"math":80,"science":75,"english":85}
print(marks.get("math"))
80
print(marks.get("history",0))
0
print(marks.get("history"))
None
for subject,score in marks.items():
    print(subject,score)

    
math 80
science 75
english 85
>>> marks.update({"math": 90})
>>> print(marks)
{'math': 90, 'science': 75, 'english': 85}
>>> #########################################################
>>> purchases={
...     "Alice":40,
...     "Bob":60,
...     "John":52}
>>> for name,amount in purchases.items():
...     print(f"{name} spent ${amount}")
... 
...     
Alice spent $40
Bob spent $60
John spent $52
>>> purchases.update({"John":500})
>>> print("After Adding John:",purchases)
After Adding John: {'Alice': 40, 'Bob': 60, 'John': 500}
>>> purchases.pop("Alice")
40
>>> print("After Removing Alice:",purchases)
After Removing Alice: {'Bob': 60, 'John': 500}
>>> ###############################################################
>>> #Taking input from user
>>> n=int(input("Enter number of customer:"))
Enter number of customer: 3
>>> user_purchases={}
>>> for i in range(n):
...     name=input("Enter customer name:")
...     amount=int(input("Enter purchases amount for {anme}:"))
...     user_purchases[name]=amount
...     print("Customer Purchases Data:",user_purchases)
... 
...     
Enter customer name:Badtuu
Enter purchases amount for {anme}:500
Customer Purchases Data: {'Badtuu': 500}
Enter customer name:Anchu
Enter purchases amount for {anme}:900
Customer Purchases Data: {'Badtuu': 500, 'Anchu': 900}
Enter customer name:summi
Enter purchases amount for {anme}:400
Customer Purchases Data: {'Badtuu': 500, 'Anchu': 900, 'summi': 400}
