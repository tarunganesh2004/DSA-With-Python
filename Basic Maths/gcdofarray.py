# GCD of an Array of Numbers
import math
from functools import reduce

def gcd_of_array(arr):
    if not arr:
        return 0
    return reduce(math.gcd, arr)

print(gcd_of_array([48,15, 18, 30]))  # Output: 6