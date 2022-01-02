#Arithmetic Conditionally: means that we can define conditions where the arithmetic operation should happen.

import numpy as np

#Add the values in arr1 to the values in arr2:
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)
print(newarr)



#Subtract the values in arr2 from the values in arr1:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)
print(newarr)



#Multiply the values in arr1 with the values in arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)
print(newarr)



#Divide the values in arr1 with the values in arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)
print(newarr)
#result of 10*10*10, 20*20*20*20*20, 30*30*30*30*30*30



# Raise the valules in arr1 to the power of values in arr2: (exponential)
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)
print(newarr)



#Both the mod() and the remainder() functions return the remainder of the values 
# in the first array corresponding to the values in the second array, and return the results in a new array.
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.mod(arr1, arr2)
print(newarr)
#he example above will return [1 6 3 0 0 27] which is the remainders when you divide 10 with 3 (10%3), 
# 20 with 7 (20%7) 30 with 9 (30%9) etc.

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

#Return the remainders
newarr = np.remainder(arr1, arr2)
print(newarr) #You get the same result when using the remainder() function:


# Return the quotient and mod:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)
print(newarr)


#Both the absolute() and the abs() functions functions do the same absolute operation element-wise 
# but we should use absolute() to avoid confusion with python's inbuilt math.abs()
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr) #The example above will return [1 2 1 2 3 4].