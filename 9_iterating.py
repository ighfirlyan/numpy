import numpy as np

#Iterate on the elements of the following 1-D array
arr = np.array([1,2,3])

for x in arr:
    print(x)

#Iterating 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

#Iterate on each scalar element of the 2-D array
for x in arr:
    for y in x:
        print(y)

#Iterating 3-D Arrays. In a 3-D array it will go through all the 2-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

#Iterate down to the scalars:
for x in arr:
    for y in x:
        for z in y:
            print(z)

#Iterating Arrays Using nditer()
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

#Iterating Array With Different Data Types
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

#Iterate through every scalar element of the 2D array skipping 1 element
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

#Enumerate on following 1D arrays elements:
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

#Enumerate on following 2D array's elements
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)