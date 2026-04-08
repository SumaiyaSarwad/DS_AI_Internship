Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list Example
numbers=[10,20,30,40]

#Tuple Example
coordinates=(5,10)
print(numbers)
[10, 20, 30, 40]
print(coordinates)
(5, 10)

#######################################################################################################################################################3
#Indexing & Slicing
a=[100,200,300,500]
a[-3:-1]
[200, 300]
a[-1:-3]
[]
a[1:4]
[200, 300, 500]

#skip
a[1:4:2]
[200, 500]
a[1:4:1]
[200, 300, 500]
a=[100,200,300,400,500,800,600,900,700]
a[1:4:3]
[200]
a[1:9:3]
[200, 500, 900]
a[1:9:2]
[200, 400, 800, 900]
a[2:9:3]
[300, 800, 700]
a[-8,9,-2]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a[-8,9,-2]
TypeError: list indices must be integers or slices, not tuple
a[-8:9:-2]
[]
a[-8,-2,2]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a[-8,-2,2]
TypeError: list indices must be integers or slices, not tuple
a[-8:-2:2]
[200, 400, 800]

#############################################################################################################################################################
#List Methods and Mutability
marks=[85,42,63,70,20,50]
marks.append(90)
print(marks)
[85, 42, 63, 70, 20, 50, 90]
marks.pop()
90
print(marks)
[85, 42, 63, 70, 20, 50]
marks.sort()
>>> print(marks)
[20, 42, 50, 63, 70, 85]
>>> marks.desc()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    marks.desc()
AttributeError: 'list' object has no attribute 'desc'
>>> marks.reverse()
>>> print(marks)
[85, 70, 63, 50, 42, 20]
>>> marks.extend()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    marks.extend()
TypeError: list.extend() takes exactly one argument (0 given)
>>> marks.extend(90)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    marks.extend(90)
TypeError: 'int' object is not iterable
>>> marks.extend(5)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    marks.extend(5)
TypeError: 'int' object is not iterable
>>> marks.insert(60,5)
>>> print(marks)
[85, 70, 63, 50, 42, 20, 5]
>>> marks.insert(5,60)
>>> print(marks)
[85, 70, 63, 50, 42, 60, 20, 5]
>>> marks.remove(70)
>>> print(marks)
[85, 63, 50, 42, 60, 20, 5]
>>> marks.extend([31])
>>> print(marks)
[85, 63, 50, 42, 60, 20, 5, 31]
>>> marks.count()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    marks.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> marks.count(31)
1
>>> len(marks)
8
