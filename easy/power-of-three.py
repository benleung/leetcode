# 1'
# same as power of two


'''
further learning

method of time complexity of O(1) --> need to recite, impossible to know in advance so skip
'''
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 3:
            if n %3 == 0:
                n //= 3
            else:
                return False
        return n == 1
