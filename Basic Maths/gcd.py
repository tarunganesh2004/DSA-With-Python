# GCD 

# without recursion
def gcd(a,b): # O(min(a,b))
    gcd=1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd

# with recursion
# gcd(a,b)=gcd(b,a mod b)
def gcd_recursive(a,b): # O(logn)
    if b==0: 
        return a
    return gcd_recursive(b, a % b)

# iterative version of euclid algorithm
def gcd_iterative(a, b):
    while b!=0:
        a,b= b, a % b
    return a

print(gcd(48, 18))  # Output: 6
print(gcd_recursive(48, 18))  # Output: 6
print(gcd_iterative(48, 18))  # Output: 6

