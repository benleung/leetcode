'''
revised on 2/24
worth do again with bit manipulation
'''


'''
6'30"

bad
missing the cases that n <=0

good
able to observe the pattern that we can divide step by step

'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 2:
            if n % 2 == 1:
                return False
            n /= 2
        return n > 0

# however, there is a better solution using bitwise operations
