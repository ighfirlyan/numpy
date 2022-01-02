#Addition is done between two arguments whereas summation happens over n elements.

#Add the values in arr1 to the values in arr2:
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.add(arr1, arr2)
print(newarr) #[2 4 6]

#Sum the values in arr1 and the values in arr2:
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(newarr) #12


# Perform summation in the following array over 1st axis:
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2], axis=1)
print(newarr) #[6 6]

#Cummulative Sum
#The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr) #[1 3 6]