#numpy
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([10,20,30])
result = a+b
print(result)

'''
Output:
    [[11 22 33]
     [14 25 36]]
'''
#######################################################

#Vectorized vs Loop example
arr=np.random.rand(1000000)

#Vectorized
squared=arr**2

######################################################
#1D and 2D arrays
arr= np.arange(12)
reshaped=arr.reshape(3,4)
print(reshaped)

'''
Output:
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
'''

#Stacking Vertically and Horizontally
a=np.array([[1,2]])
b=np.array([[3,4]])
vstacked=np.vstack((a,b))
print(vstacked)

'''
Output:
    [[1 2]
     [3 4]]
'''

#######################################################
#Statistical Functions in Numpy
data=np.array([[10,20,30],[40,50,60]])
print(np.mean(data))
print(np.mean(data,axis=0))

'''
Output:
    35.0
    [25. 35. 45.]
'''
########################################################
#Linear Algebra Basics with Numpy
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
print(np.dot(A,B))

'''
Output:
    [[19 22]
     [43 50]]
'''
