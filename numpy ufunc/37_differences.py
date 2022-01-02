# A discrete difference means subtracting two successive elements.
#E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]

import numpy as np

#Compute discrete difference of the following array
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr) #[5 10 -20] because 15-10=5, 25-15=10, and 5-25=-20

#Compute discrete difference of the following array twice
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)
print(newarr) #[5 -30] because: 15-10=5, 25-15=10, and 5-25=-20 AND 10-5=5 and -20-10=-30