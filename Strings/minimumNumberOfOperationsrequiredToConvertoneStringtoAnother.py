# https://www.geeksforgeeks.org/minimum-number-of-given-operations-required-to-convert-a-string-to-another-string/?ref=asr1
S="011"
T="101" # minimum operations == 1

# def min_operations(s,t):
#     n1=len(s)
#     n2=len(t)
#     if n1!=n2:
#         return -1
    
#     c1=[0]*2
#     c2=[0]*2

#     for i in range(n1):
#         c1[int(s[i])]+=1
#         c2[int(t[i])]+=1

#     if c1[0]!=c2[0] or c1[1]!=c2[1]:
#         return -1
    
#     swap_needed=0
#     for i in range(n1):
#         if s[i]!=t[i]:
#             swap_needed+=1

#     return (swap_needed+1)//2

# print(min_operations(S,T)) # 1

def another_way(s,t):
    ct0=0
    ct1=0

    for i in range(len(s)):
        if s[i]==t[i]:
            continue

        if s[i]=='0':
            ct0+=1
        else:
            ct1+=1

    return max(ct0,ct1)

print(another_way(S,T)) # 1

s1="001101"
s2="101001" # 2

print(another_way(s1,s2)) # 2
print(another_way("010","101"))