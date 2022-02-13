'''
within 5'

bottomup, non-optiomized dp

question: what is the time complexity without memorization and dp
2^n, because Each call to F(n) makes 2 additional calls, to F(n - 1) and F(n - 2). Those 2 calls will then generate 4 calls, which will generate 8, etc



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
