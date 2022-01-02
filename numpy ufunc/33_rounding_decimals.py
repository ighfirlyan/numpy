import numpy as np

#Truncation
#Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
arr = np.trunc([-3.1666, 3.6667])
print(arr) #returns integers

#Same example, using fix()
arr =  np.fix([-3.1666, 3.6667])
print(arr)

#Rounding
# The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
# Round off 3.1666 to 2 decimal places
arr = np.round(3.1666,2)
print(arr)

# Floor
# The floor() function rounds off decimal to nearest lower integer.
arr = np.floor([-3.1666, 3.6667])
print(arr) #returns floats

#Ceil
#The ceil() function rounds off decimal to nearest upper integer.
arr = np.ceil([-3.1666, 3.6667])
print(arr)