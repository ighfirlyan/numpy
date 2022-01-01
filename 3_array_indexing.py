import numpy as np
from numpy.core.defchararray import array

arr = np.array([1,2,3,4])

#Get the first element from the following array
print(arr[0])

#Get the second element from the following array.
print(arr[1])

#Get third and fourth elements from the following array and add them
print(arr[2] + arr[3])


#Access 2-D Arrays
#Access the element on the first row, second column
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print('2nd element on 1st row : ', arr[0,1])

#Access the element on the 2nd row, 5th column
print('5th element on 2st row : ', arr[1,4])


#Access 3-D arrays
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)

#Access the third element of the second array of the first array
print('3rd element of the 2nd array of the 1st array: ', arr[0,1,2])

#Negative Indexing
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print('Last element from 2nd dimension : ', arr[1,-1])