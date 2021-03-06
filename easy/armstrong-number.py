'''
revised on 2/23
'''

'''
second try: 3'
'''
from functools import reduce

class Solution(object):
    def isArmstrong(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str(n)
        digits = len(s)
        return n == reduce(lambda x, y: x + int(y)**digits, s, 0)
