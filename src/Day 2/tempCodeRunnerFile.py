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
