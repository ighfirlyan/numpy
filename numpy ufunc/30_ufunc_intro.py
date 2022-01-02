#ufuncs stands for "Universal Functions" and they are NumPy functions that operates on the ndarray object.

# ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
# They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.
# ufuncs also take additional arguments, like:
# where boolean array or condition defining where the operations should take place.
# dtype defining the return type of elements.
# out output array where the return value should be copied.

# Without ufunc, we can use Python's built-in zip() method:
x = [1,2,3,4,5]
y = [4,5,6,7,8]
z = []

for i,j in zip(x,y):
    z.append(i+j)

print(z)

# With ufunc, we can use the add() function:
import numpy as np

x = [1,2,3,4,5]
y = [4,5,6,7,8]
z = np.add(x,y)
print(z)