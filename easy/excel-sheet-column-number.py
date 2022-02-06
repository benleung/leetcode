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
