
'''
7' knowing the hint and copy and paste from house-robber

learn
- for start and end adjacent problem, remember this trick
  the hint of Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. Now the problem has degenerated to the House Robber, which is already been solved. -> is everything
  -> 
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # 0~N-2
        N = len(nums)
        dp = [0]*(N+1)
        dp[N-2] = nums[N-2] # assume nums[N-1] doesn't exist
        for i in range(N-3,-1,-1):
            dp[i] = max(dp[i+1], nums[i]+dp[i+2])
        # exclude last house
        
        withoutLast = dp[0]
        
        # 1~N-1
        dp[N-1] = nums[N-1] # assume nums[N-1] doesn't exist
        for i in range(N-2,0,-1):
            dp[i] = max(dp[i+1], nums[i]+dp[i+2])
        # exclude last house
        
        withoutFirst = dp[1]
        
        
        return max(withoutLast, withoutFirst)
        
        