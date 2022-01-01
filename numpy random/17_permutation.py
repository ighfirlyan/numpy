from numpy import random
import numpy as np

#Randomly shuffle elements of following array
arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr) #The shuffle() method makes changes to the original array.

#Generate a random permutation of elements of following array
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr)) #The permutation() method returns a re-arranged array (and leaves the original array un-changed).

