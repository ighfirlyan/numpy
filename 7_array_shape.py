import numpy as np
from numpy.core.fromnumeric import ndim

arr = np.array([[1,2,3,4],[5,6,7,8]])

#Print the shape of a 2-D array
print(arr.shape) 
#will print (2,4) means that the array has 2 dimensions, 
#where the first dimension has 2 elements and the second has 4.

#Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 
#and verify that last dimension has value 4
arr = np.array([1,2,3,4], ndmin=5)
print(arr)
print('Shape of array : ', arr.shape)

