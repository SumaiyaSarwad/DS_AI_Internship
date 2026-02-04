#SIMPLE CALCULATOR
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    sum= num1 + num2
    print("Result:",sum)
elif operator == "-":
    difference= num1 - num2
    print("Result:",difference)
elif operator == "*":
    product= num1 * num2
    print("Result:",product)
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")

#Output: Enter first number: 6
#        Enter second number: 5
#        Enter operator (+, -, *, /): +
#        Result: 11.0


######################################################################################################

#CONCATENATION
name=input("Enter the name:")
print("Welcome,",name)
print("Welcome,"+name)
# can also be done by using & and 'cont'

#Output: Enter the name:sumaiya
#        Welcome, sumaiya
#        Welcome,sumaiya

######################################################################################################

#TYPE CASTING
#we can convert integer to complex numbers
#floating can be converted to complex
# but vice versa is not possible
#why typecasting
a=input("Enter a number:")
b=complex(a)
print(a)
print(b)

#Output: Enter a number:4
#        4
#       (4+0j)
