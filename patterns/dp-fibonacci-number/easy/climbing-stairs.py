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

'''
11'
dp (without optimization)
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*n
        if n == 1:
            return 1
        
        dp[n-1] = 1
        dp[n-2] = 2
        
        for i in range(n-3,-1,-1):
            dp[i] = dp[i+1] + dp[i+2]
        
        return dp[0]

'''
optimized dp
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*n
        if n == 1:
            return 1
        
        a = 1
        b = 2
        
        for i in range(n-3,-1,-1):
            b, a = a + b, b
        
        return b
