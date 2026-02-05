#Task 1: The Personal Contact Book (Dictionaries)
Contacts= {"Alice":123456,"Bob":789123,"David":456789}
print("Contacts:",Contacts)

Contacts.update({"Charlie":589641})
print("After adding new contact:",Contacts)

Contacts.update({"Alice": 1000001})
print("After updating Alice's number:",Contacts)

print(Contacts.get("Alice"))
print(Contacts.get("John","Contact not found."))

for Name,Number in Contacts.items():
    print(f"Contact:{Name}|Phone:{Number}")

#Output: Contacts: {'Alice': 123456, 'Bob': 789123, 'David': 456789}
    
#        After adding new contact: {'Alice': 123456, 'Bob': 789123, 'David': 456789, 'Charlie': 589641}
#        After updating Alice's number: {'Alice': 1000001, 'Bob': 789123, 'David': 456789, 'Charlie': 589641}

#        1000001
#        Contact not found.

#        Contact:Alice|Phone:1000001
#        Contact:Bob|Phone:789123
#        Contact:David|Phone:456789
#        Contact:Charlie|Phone:589641


