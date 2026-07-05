# Divisors of a Number

# brute force O(n)
def divisors(n):
    f=[]
    for i in range(1, n + 1):
        if n % i == 0:
            f.append(i)
    return f

# optimized O(sqrt(n))
def divisors_optimized(n):
    f = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            f.append(i)
            if i != n // i:  # Avoid adding the square root twice
                f.append(n // i)
    return sorted(f)  # Return sorted list of divisors

