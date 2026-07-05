# s1="ABC123"
# s2="DD"

# l1=[0]*128
# for c in s1:
#     l1[ord(c)-ord('a')]+=1

# l2=[0]*128
# for c in s2:
#     l2[ord(c)-ord('a')]+=1

# print(l1)
# print(l2)

# cost=0
# for i in range(128):
#     cost+=abs(l1[i]-l2[i])

# print(cost) # 8

s1="Hello 123 902#04      "
print(len(s1))
print(len(s1.strip())) # 15
print(s1.split(' '))

