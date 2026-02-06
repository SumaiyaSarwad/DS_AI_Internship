#Function
#this is default function, because it doesnot have any parameters
def greet():
    print("Hello,welcome to the internship!")
greet()

#Output:Hello,welcome to the internship!

#############################################################################
#Arguments and Return Values
def add_num(a,b):
    return a+b
result =add_num(3,4)
print(result)

#Output:7

#############################################################################
#Variable Scope
x=10
def show_value():
    x=5
    print(x)
show_value()
print(x)

#Output:5
#      10


#Local and Global Variables
Animal ="Dog"
def human():
    Bird="Crow"
    Fly="Peacock"
    print(f"{Bird} flies.")
human()
print(f"{Animal} barks.")
print(f"{Fly} flies.")

#Output: Crow flies.
#        Dog barks.
#        NameError: name 'Fly' is not defined
###########################################################################
#Importing Standard Modules
import math
import random
print(math.sqrt(16))
print(random.randint(1,10))

#Output: 4.0
#        6
