# Trigonometric Functions
# NumPy provides the ufuncs sin(), cos() and tan() 
# that take values in radians and produce the corresponding sin, cos and tan values.


import numpy as np


#Find sine value of PI/2:
x = np.sin(np.pi/2)
print(x)


#find sine values for all of the values in array
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)

#Convert Degrees Into Radians. radians values are pi/180 * degree_values.
#Convert all of the values in following array arr to radians
arr = np.array([90,180,270,360])
x = np.deg2rad(arr)
print(x)

# Radians to Degrees
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)

#Finding Angles
x = np.arcsin(1.0)
print(x)

#Angles of Each Value in Arrays
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)

# Find the hypotenues for 4 base and 3 perpendicular:
base = 3
perp = 4
x = np.hypot(base, perp)

print(x)