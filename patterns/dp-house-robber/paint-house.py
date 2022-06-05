'''
12'
making decision that will affect the adject house
'''
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        '''
        red, blue, or green
        0 1 2
        '''
        C = len(costs)
        dp = [[0]*3 for _ in range(C)]
        for i in range(3):
            dp[0][i] = costs[0][i]
        
        for i in range(1, C):
            dp[i][0] = costs[i][0]+  min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs[i][1]+  min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs[i][2]+  min(dp[i-1][0], dp[i-1][1])
        
        return min(dp[C-1][0], dp[C-1][1], dp[C-1][2])
