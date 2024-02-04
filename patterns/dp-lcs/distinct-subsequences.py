'''
solve myself, very good question (similar to classic lcs, and require knowledge on combination)

comb(a, b)
= comb(a-1, b-1) + comb(a-1, b)


rabbbb
rabb

1) comb(a-1, b-1): use the new element in the sequence combination
rabbb b
      _
rab   b
      _

2) comb(a-1, b): the new element in the sequence combination
rabbb b
  ___
rabb
   _

'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        S = len(s)+1
        T = len(t)+1
        
        dp = [[0]*S for _ in range(T)]
        for i in range(S):
            dp[0][i] = 1
        for i in range(1, T):
            for j in range(1, S):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]



                else:
                    dp[i][j] = dp[i][j-1]

        return dp[T-1][S-1]
