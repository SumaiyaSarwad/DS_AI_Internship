#Task 2: The Reshaper (Array Manipulation)
import numpy as np

data = np.arange(24)
reshaped = data.reshape(4, 3, 2)
final_array = reshaped.transpose(0, 2, 1)

print("Final Shape:", final_array.shape)
print("Final Array:\n", final_array)

'''
Output:
    Final Shape: (4, 2, 3)
    Final Array:
     [[[ 0  2  4]
      [ 1  3  5]]

     [[ 6  8 10]
      [ 7  9 11]]

     [[12 14 16]
      [13 15 17]]

     [[18 20 22]
      [19 21 23]]]
'''


