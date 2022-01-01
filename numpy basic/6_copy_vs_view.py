import numpy as np

arr = np.array([1, 2, 3, 4, 5])

#Make a copy, change the original array, and display both arrays
x = arr.copy()
arr[0] = 42

print(arr)
print(x) #The copy SHOULD NOT be affected by the changes made to the original array

#Make a view, change the original array, and display both arrays:
x = arr.view()
arr[0] = 42

print(arr)
print(x)

#Make a view, change the view, and display both arrays
x = arr.view()
x[0] = 31

print(arr)
print(x)

#Print the value of the base attribute to check if an array owns it's data or not
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base) #copy returns none
print(y.base) #view return the original array