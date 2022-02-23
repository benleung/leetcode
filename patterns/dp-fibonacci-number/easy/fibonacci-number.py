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

'''
within 2'

'''
class Solution:
    def fib(self, n: int) -> int:
        prev = 0
        cur = 1
        
        if n == 0:
            return 0
        
        for i in range(2,n+1):
            prev, cur = cur, cur + prev
        
        return cur
