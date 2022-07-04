'''
should try again
fail to solve

explaination

dp[i]: number of people who once know secret at day i+1 (exclude those who forget)
'''
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = defaultdict(int) # dp[i]: number of people who know secret (includes forgotten ones, aka "ghost") at day i+1
        dp[0] = 1

        for i in range(1,n):
            # dp[i-delay]: number of people (including ghost) capable to share secret on day i 
            # dp[i-forget]: number of ghost on day i 
            dp[i] = dp[i-1] + dp[i-delay] - dp[i-forget]
        
        return (dp[n-1] - dp[n-1-forget]) % 10**9+7
