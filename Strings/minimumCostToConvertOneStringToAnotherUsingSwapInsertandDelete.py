# Minimum cost to convert one string to another using swap, insert and delete operations
# a character of string a can be swapped from another character of the same string cost=0
# a character can be deleted from string b or can be inserted in string a. cost=1
from collections import Counter
A="1aB+-"
B="CC" # output : remove all 5 characters from A and insert 2 characters in A. cost=5+2=7

def minCost(A,B):
    c1=Counter(A)
    c2=Counter(B)

    # find the common characters in both strings
    common=set(A)&set(B)
    cost=0
    for ch in common:
        cost+=abs(c1[ch]-c2[ch])

    # find the characters in A but not in B
    diff=set(A)-set(B)
    for ch in diff:
        cost+=c1[ch]

    # find the characters in B but not in A
    diff=set(B)-set(A)
    for ch in diff:
        cost+=c2[ch]
    
    return cost

print(minCost(A,B)) # 7

def anotherWay(s1,s2):

    l1=[0]*128
    for c in s1:
        l1[ord(c)-ord('a')]+=1
    
    l2=[0]*128
    for c in s2:
        l2[ord(c)-ord('a')]+=1

    cost=0
    for i in range(128):
        cost+=abs(l1[i]-l2[i])

    return cost

print(anotherWay(A,B)) # 7