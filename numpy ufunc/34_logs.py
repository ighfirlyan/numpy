import numpy as np

#Find log at base 2 of all elements of following array
arr = np.arange(1, 10)
print(np.log2(arr))
#The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included).


# Find log at base 10 of all elements of following array
arr = np.arange(1, 11)
print(np.log10(arr)) #log10(10) adalah 1

#Find log at base e of all elements of following array:
arr = np.arange(1, 10)
print(np.log(arr))


# Log at Any Base
# NumPy does not provide any function to take log at any base, 
# so we can use the frompyfunc() function along with inbuilt function math.log() 
# with two input parameters and one output parameter
from math import log

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))