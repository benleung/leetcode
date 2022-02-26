
'''
15'30" to code ( some more time to think of solution somewhere else)

good
- think of solution without any hints
- pass without too many fails

bad
- mistake of using dp[N]=0 isntead of dp[N]=1
- 
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        if N == 0:
            return 0

        dp = [1]*(N+1) # dp[N] = 1 (often mistake here: 1 instead of 0 to represent this check is successfully)
        dp[N-1] = 1 if self.check(s[N-1]) else 0 # one character 0~9, still exist possibility of not alphabet
        for i in range(N-2,-1,-1):
            dp[i] = 0
            if self.check(s[i]):
                dp[i] += dp[i+1]
            if len(s[i:i+2]) ==2 and self.check(s[i:i+2]):
                dp[i] += dp[i+2]
        
        return dp[0]
        
    def check(self, s):
        N = len(s)
        if N == 0 or N>=3:
            return False
        if N == 2 and s[0] == "0":
            return False
        return 1<=int(s)<=26
