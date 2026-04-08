#Task 1: The Personal Logger (Appending & Modes)
name = input("Enter your name: ")
daily_goal = input("Enter your daily goal: ")

with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Daily Goal: {daily_goal}\n")

print("Entry saved successfully!")

'''
Output:
= RESTART: B:\AIML Internship\src\Day 7\Task 1_The Personal Logger (Appending & Modes).py
Enter your name: Sumaiya
Enter your daily goal: Finish Python file handling
Entry saved successfully!

= RESTART: B:\AIML Internship\src\Day 7\Task 1_The Personal Logger (Appending & Modes).py
Enter your name: Sumaiya
Enter your daily goal: Practice CSV and Excel handling
Entry saved successfully!

= RESTART: B:\AIML Internship\src\Day 7\Task 1_The Personal Logger (Appending & Modes).py
Enter your name: Sumaiya
Enter your daily goal: Revise append vs write modes
Entry saved successfully!
'''

'''
Name: Sumaiya, Daily Goal: Finish Python file handling
Name: Sumaiya, Daily Goal: Practice CSV and Excel handling
Name: Sumaiya, Daily Goal: Revise append vs write modes
'''

