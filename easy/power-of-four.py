# 1'
# there is better solution wiht time complexity O(1)
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 4:
            if n%4 == 0:
                n //= 4
            else:
                return False
        
        return n == 1
