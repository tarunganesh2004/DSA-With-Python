# Sum of digits

def sum_of_digits(n): # TC O(d)==>O(logn), where d is the number of digits in n
    # n%10 gives the last digit
    # n//10 removes the last digit
    total=0
    while n>0:
        rem=n%10
        total+=rem
        n=n//10
    return total

def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev

def armstrong(n):
    total=0
    num_digits=len(str(n))  # Count the number of digits
    original_n = n  # Store the original number for comparison
    while n>0:
        digit=original_n % 10
        total += digit ** num_digits
        original_n //= 10
    return total == n


