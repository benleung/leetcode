'''
within 5'

bottomup, non-optiomized dp
'''

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]