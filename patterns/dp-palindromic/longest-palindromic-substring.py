'''
about 1 hour

techniques
- it is possible to work out the way to expand the dp, by running 2 for loop, by incrementing length of string, and incrementing starting index 
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = [[True]*N for _ in range(N)]
        
        ans = s[0]
        maxLen = 0
        
        for i in range(N-1):
            dp[i][i+1] = s[i] == s[i+1]
            if dp[i][i+1] and 2 > maxLen:
                maxLen = 2
                ans = s[i:i+2]
        for i in range(2,N):
            for j in range(0,N-i):
                dp[j][i+j] = dp[j+1][i+j-1] and s[j] == s[i+j]
                if dp[j][i+j] and i+1 > maxLen:
                    ans = s[j:j+i+1]
        
        return ans
