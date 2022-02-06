
'''
40'

learning
- initialize 2d list in a right way
- inital border
- be careful of the flow of for loop to see if possible to go to somewhere neighbour element is not defined yet
'''

def d(dp, i, j):
    if i < 0 or j < 0:
        return 0   # tips: initial border
    else:
        return dp[i][j]

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        I = len(text1)
        J = len(text2)
        # dp[i][j] means the number of common subsequence of text1[0..i] and text2[0..j]
        dp = [[0]*J for _ in range(I)]
        
        for i in range(I):
            for j in range(J):
                if text1[i] == text2[j]:
                    dp[i][j] = d(dp,i-1, j-1) + 1
                else:
                    dp[i][j] = max(d(dp,i-1,j), d(dp,i,j-1))
        
        
        return dp[I-1][J-1]

'''
13' knew the hint and trick point in advance
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        I = len(text1)
        J = len(text2)
        dp = [[0]*(J+1) for _ in range(I+1)]
        for i in range(1,I+1):
            for j in range(1,J+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[I][J]
