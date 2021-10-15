from math import factorial

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        a = 0
        b = 0
        while 2*a <= n:
            while b <= n:
                if 2 * a + b == n:
                    count += factorial(a+b) / factorial(b) / factorial(a)
                b += 1
            a += 1
            b = 0
        return count