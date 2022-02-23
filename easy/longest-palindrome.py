'''
5'
'''

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        h = Counter(s)
        hasOddNumber = 0
        count = 0
        
        for k,v in h.items():
            hasOddNumber = hasOddNumber or v % 2
            count += v - v%2
        
        return count + (1 if hasOddNumber else 0)
