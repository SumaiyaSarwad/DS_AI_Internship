Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name=input("Enter the name:")
Enter the name: Sumaiya 
>>> print("Welcome,",name)
Welcome,  Sumaiya 
>>> print("Welcome,"+name)
Welcome, Sumaiya 
>>> print("Welcome,"&name)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print("Welcome,"&name)
TypeError: unsupported operand type(s) for &: 'str' and 'str'
>>> print("Welcome,"&"name")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print("Welcome,"&"name")
TypeError: unsupported operand type(s) for &: 'str' and 'str'
>>> print("Welcome," cont name)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
