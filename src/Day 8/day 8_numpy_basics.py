###################################
# 1D Array
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("1D NumPy Array:", arr)

'''
Output:
   1D NumPy Array: [1 2 3 4 5]
'''

# 2D Array
arr_2d = np.array([[1, 2], [3, 4]])
print("2D NumPy Array:\n", arr_2d)

'''
Output:
    2D NumPy Array:
     [[1 2]
     [3 4]]
'''

# 0D, 1D, 2D, 3D Arrays
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("\n ",a)
print("\n",b)
print("\n",c)
print("\n",d)

'''
Output:
   42

  [1 2 3 4 5]

  [[1 2 3]
  [4 5 6]
  [7 8 9]]

  [[[1 2 3]
   [4 5 6]]

  [[1 2 3]
   [4 5 6]]]
'''

#ndim-tells how many dimensions array has!!
print(a.ndim)  # 0D
print(b.ndim)  # 1D
print(c.ndim)  # 2D
print(d.ndim)  # 3D

'''
Output:
    0
    1
    2
    3
'''

#shape-tells how many elements are there!
arr=np.array([1,2,3,4,6,7])
print(arr.shape)

'''
Output:
    (6,)
'''

# Simple Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row:', arr[0, 1]) #arr[row,column]

'''Output:
    2nd element on 1st row: 2
'''

# 3D Indexing
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[1, 0, 2]) # arr[axis,row,column]

'''
Output:
    9
'''

# 1D Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

'''
Output:
    [2 3 4 5]
'''

# Using arange (Start, Stop, Step)
arr = np.arange(40, 55, 3)
print("Array of numbers:", arr)
#two dimensional array
print(arr.shape)
arr_1 =np.arange(1,17).reshape(4,4)
print(arr_1)

'''
Output:
    Array of numbers: [40 43 46 49 52]
    (5,)
    [[ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]
     [13 14 15 16]]
'''

#create 3d array using arange function
arr = np.arange(0, 12, 2)
print(arr)
print("Shape before reshape:", arr.shape)

arr3d = arr.reshape(1, 2, 3)
print("Shape after reshape:", arr3d.shape)
print(arr3d)

'''
Output:
    [ 0  2  4  6  8 10]
    Shape before reshape: (6,)
    Shape after reshape: (1, 2, 3)
    [[[ 0  2  4]
    [ 6  8 10]]]
'''


# Using linspace (Evenly spaced)
arr = np.linspace(0, 2, 5)
print(arr)

'''
Output:
    [0.  0.5 1.  1.5 2. ]
'''

# Random values
#rand() → Only floats in [0, 1)-generates a 2×2 array (matrix) filled with random numbers between 0 and 1.
arr = np.random.rand(2, 2)
print(arr)

'''
Output:
    [[0.74843656 0.57208807]
     [0.52061579 0.69024013]]
'''

#np.random.randn()	- Normal (Gaussian) distribution	Covers negative and positive values(not evenly distributed)
import numpy as np

arr = np.random.randn(2, 3)
print(arr)

'''
Output:
    [[-0.31597115 -0.63129013  0.92327277]
    [-0.01082646  0.67851839  0.79569026]]
'''

#uniform-Use uniform(low, high, size=...) for floats
arr = np.random.uniform(20, 30, size=(2, 2))
print(arr)
print(arr.dtype)

'''
Output:
    arr = np.random.uniform(20, 30, size=(2, 2))
    print(arr)
    print(arr.dtype)
'''

#randint- Use randint(low, high, size=...) for integers
arr = np.random.randint(10, 15, size=(3, 3))
print(arr)
print(arr.size)

'''
Output:
    [[14 12 14]
    [11 14 14]
    [13 11 12]]
    9
'''

# Array Inspection
arr = np.array([[1, 2], [3, 4]])
print(arr.shape)  # Shape (rows, columns)


'''
Output:
    (2,2)
'''

arr = np.array([1, 2, 3])
print(arr.dtype)  # Data type

'''
Output:
    int64
'''

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.size)  # Total number of elements

'''
Output:
    6
'''

#Array Operations & Broadcasting
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)  # Element-wise addition
print("Multiplication by scalar:", a * 2)
print("Element-wise multiplication:", a * b)
print("Mean of array a:", np.mean(a))

'''
Output:
    Addition: [11 22 33]
    Multiplication by scalar: [20 40 60]
    Element-wise multiplication: [10 40 90]
    Mean of array a: 20.0
'''

# Universal Functions (ufuncs)
arr = np.array([1, 4, 9])
print(np.sqrt(arr))  # Square root

'''
Output:
    [1. 2. 3.]
'''

arr = np.array([0, np.pi/2])
print(np.sin(arr))  # Sine

'''
Output:
    [0. 1.]
'''

arr = np.array([1, 2])
print(np.exp(arr))  # Exponential

'''
Output:
    [2.71828183 7.3890561 ]
'''


#np.floor()-Rounds down to the nearest integer.
arr = np.array([1.2, 2.8, -3.7])
print(np.floor(arr))

'''
Output:
    [ 1.  2. -4.]
'''

#np.ceil()-Rounds up to the nearest integer.
arr = np.array([1.2, 2.8, -3.7])
print(np.ceil(arr))
print("trunc",np.trunc(arr))#removes only the decimal
print("round",np.round(arr))

'''
Output:
    [ 2.  3. -3.]
   trunc [ 1.  2. -3.]
   round [ 1.  3. -4.]
'''

#np.log()-Returns the natural logarithm (base e) of each element.-[1, e, e²]-
#np.e → This is Euler's number ≈ 2.718
#np.e**2 → e² ≈ 7.389
arr = np.array([1, np.e, np.e**2])
print(np.log(arr))

'''
Output:
    [0. 1. 2.]
'''



    
    