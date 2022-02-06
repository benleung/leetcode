'''
44'

good
- thought of optimal sol in quite early stage

bad
- careless mistake on >= 0

lean
- pattern for skip tag (edge case to handle)(1. possible to skip the skip tag   2. possible to reach the skip tag right after skipping)

'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s)-1
        j = len(t)-1
        
        countS = 0
        countT = 0
        
        while i>=0 or j>=0:
            while i>=0 and s[i] == "#":
                countS += 1
                i -= 1
            while countS>0 and not (i>0 and s[i] == "#"):
                countS -= 1
                i -= 1
            if i>=0 and s[i] == "#":
                continue
                
            while j>=0 and t[j] == "#":
                countT += 1
                j -= 1
            while countT>0 and not (j>0 and t[j] == "#"):
                countT -= 1
                j -= 1
            if j>=0 and t[j] == "#":
                continue
            
            if i<0 and j<0:
                return True

            if (i<0 and j>=0) or (j<0 and i>=0):
                return False
            if s[i] != t[j]:
                return False
            
            i -= 1
            j -= 1
            
        return True
