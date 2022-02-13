'''
13'

good 
able to write lcs quickly (even some of the parts are forgotten)


bad
since using N+1 to simplify dp initialization, word1[j-1] instead of word1[j] was used

'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)
        dp = [[0]*(M+1) for _ in range(N+1)]
        for i in range(1,M+1):
            for j in range(1,N+1):
                if word1[j-1] == word2[i-1]:
                    dp[j][i] = dp[j-1][i-1] + 1
                else:
                    dp[j][i] = max(dp[j-1][i],dp[j][i-1])
        return N + M - 2*dp[N][M]
