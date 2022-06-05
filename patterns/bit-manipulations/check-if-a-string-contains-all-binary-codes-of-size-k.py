'''
5'
'''
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        window = int(s[:k], 2)
        
        sets = set([window])
        
        for i in range(k, len(s)):
            window = ((window << 1) + int(s[i])) & (2**k - 1)
            sets.add(window)
        
        return len(sets) == 2**k
