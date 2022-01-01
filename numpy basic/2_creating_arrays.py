import numpy as np

#creating array with list
arr = np.array(
    [1,2,3,4,5]
)

print(arr)
print(type(arr))

#creating array with tupple
arr1 = np.array(
    (1,2,3,4,5)
)

print(arr1)

#0-D arrays
arr2 = np.array(45)

print(arr2)

#1-D arrays
arr3 = np.array(
    [1,2,3,4,5,]
)

print(arr3)

#2-D arrays
arr4 = np.array([
    [1, 2, 3], 
    [4, 5, 6]
])

print(arr4)

#3-D arrays
#An array that has 2-D arrays (matrices) as its elements is called 3-D array.
arr5 = np.array([
    [[2,3,4],
    [4,5,6]],

    [[1,2,3],
    [4,5,6]]  
])

print(arr5)

#Check how many dimensions the arrays have
a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3], [4,5,6]],[[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#create an array
arr = np.array([1,2,3,4,5], ndmin=5)

print(arr)
print('number of dimensions : ', arr.ndim)