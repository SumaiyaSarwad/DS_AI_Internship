Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Task 2: The Data Slicer
>>> temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
>>> temperatures[0]
22
>>> temperatures[-1]
22
>>> temperatures[3:6]
[28, 30, 29]
>>> temperatures[-3:]
[26, 24, 22]
>>> print("first reading:",temperatures[0])
first reading: 22
>>> print("last reading:",temperatures[-1])
last reading: 22
>>> print("Afternoon Peak:",temperatures[3:6])
Afternoon Peak: [28, 30, 29]
>>> print("Last 3 Hours:",temperatures[-3:])
Last 3 Hours: [26, 24, 22]
