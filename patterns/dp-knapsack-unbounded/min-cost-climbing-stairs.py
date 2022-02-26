'''
about 6'

good to define 
"min cost dptotal to climb from ith step"
instead of 
"minimum cost to reach for ith or i+1th"

'''


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0] * (N+1) # min cost dptotal to climb from ith step
        dp[N-1] = cost[N-1]
        
        for i in range(N-2, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        return min(dp[0],dp[1])
