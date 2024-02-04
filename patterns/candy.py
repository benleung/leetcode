class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        
        dp = [None]*N
        
        def dfs(i):
            right = dfs(i+1) if i+1 < N and ratings[i] > ratings[i+1] else 0 
            left = dp[i-1] if i > 0 and ratings[i-1] < ratings[i] else 0
            
            dp[i] = max(left, right) + 1
            
            return dp[i]
        
        for i in range(N):
            if dp[i] = None:
                dp[i] = dfs(i) 
        
        return sum(dp)
