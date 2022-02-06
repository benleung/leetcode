'''
finish in 3min
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
'''
O(1) memory

learn about how to convert an exisiting solution into O(1) one
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        dp = [0]*(3)  # remove unnecessary size
        # dp[0] = 0
        dp[1] = 0  # was 1 move down
        dp[2] = 1 # was 1, move down
        cur = 1 # new variable
        for i in range(3, n+1):
            dp[0], dp[1], dp[2] = dp[1], dp[2], cur  # swap
            cur = dp[0] + dp[1] + dp[2]
        return cur
