import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

#Reshape From 1-D to 2-D
#The outermost dimension will have 4 arrays, each with 3 elements
newarr = arr.reshape(4,3)

print(newarr)

#Reshape From 1-D to 3-D
#The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements
newarr = arr.reshape(2,3,2)
print(newarr)

#Check if the returned array is a copy or a view:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)
#above returns the original array, so it is a view


#unknown dimension
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)#We can not pass -1 to more than one dimension.

print(newarr) 

#Flattening the arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)