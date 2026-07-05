# lCM
import math 
from functools import reduce

def lcm(a,b):
    return (a * b) // math.gcd(a, b)

def lcm_of_array(arr):
    if not arr:
        return 0
    return reduce(lcm, arr)

