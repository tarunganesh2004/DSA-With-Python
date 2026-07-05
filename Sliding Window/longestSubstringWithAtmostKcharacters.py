# Longets Substring with atmost K distinct characters

s="eceba"
k=2

def longestSubstringWithAtmostKCharacters(s, k):
    n=len(s)
    count = {}
    left, max_len = 0, 0
    for right in range(n):
        count[s[right]] = count.get(s[right], 0) + 1
        
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
            
        max_len = max(max_len, right - left + 1)
    return max_len

print(longestSubstringWithAtmostKCharacters(s, k))  