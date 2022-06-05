'''
intuitive
'''
class Solution(object):
    def minFallingPathSum(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        
        def minVal(r, c):
            if r >= R:
                return 0
            if not (0<=c<C):
                return inf # not avaiable choice
            return dp[r][c]
        
        dp = [[0]*C for _ in range(R)]
        for r in range(R-1, -1, -1):
            for c in range(C):
                dp[r][c] = min([
                    minVal(r+1, c-1),
                    minVal(r+1, c),
                    minVal(r+1, c+1)
                ]) + matrix[r][c]
        
        ans = inf
        for col in range(C):
            ans = min(ans, dp[0][col])
        return ans
