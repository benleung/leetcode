'''
2/21 revised
'''


# 8 min
# a small mistake on converting 26 or 27 (26 variations so this is correct(not start from 0))
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        sol = 0
        for index, ch in enumerate(columnTitle):
            sol += self.toNumber(ch) * 26**(len(columnTitle)-index-1 )
        return sol
    def toNumber(self, ch):
        return ord(ch)-64

'''
4'
almost perfect for easy question!
- technqiue for going digit by digit, and *base for each instead of using **
- ord('a')
'''
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        
        def chToNumber(c):
            return ord(c) - ord('A') + 1
        
        for c in columnTitle:
            ans *= 26
            ans += chToNumber(c)
        return ans
