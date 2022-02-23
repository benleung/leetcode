'''
rolling prev and cur

'''

from collections import defaultdict
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        S = len(s)
        count = 0
        
        ch = s[0]
        preCount = 0
        curCount = 0
        
        for c in s:
            if ch == c:
                curCount += 1
            else:
                count += min(preCount,curCount)
                preCount = curCount
                curCount = 1
                ch = c
        count += min(preCount,curCount)
        
        return count
