#Task 3: The "Safe Opener" (Error Handling)
try:
    with open("config.txt","r")as file:
        print(file.read())
except FileNotFoundError:
        print("Oops! That file doesn't exist yet.")

'''
Output:
Oops! That file doesn't exist yet.
'''
