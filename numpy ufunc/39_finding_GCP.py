# Finding GCD (Greatest Common Denominator)
# The GCD (Greatest Common Denominator), 
# also known as HCF (Highest Common Factor) is the biggest number that is a common factor of both of the numbers.

import numpy as np

# Find the HCF of the following two numbers
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)

#Finding GCD in Arrays
arr = np.array([20,8,32,36,16])
x = np.gcd.reduce(arr)

print(x)