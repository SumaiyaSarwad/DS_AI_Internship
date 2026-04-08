#Task 2: The "Duplicate Cleaner" (Sets)
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
print("List:",raw_logs)

unique_users=set(raw_logs)
print("Set:",unique_users)

if "ID05" in unique_users:
    print("True")
else: "False"

print(len(raw_logs))
print(len(unique_users))


#Output: List: ['ID01', 'ID02', 'ID01', 'ID05', 'ID02', 'ID08', 'ID01']
#        Set: {'ID01', 'ID05', 'ID08', 'ID02'}
#        True
#        7
#        4


