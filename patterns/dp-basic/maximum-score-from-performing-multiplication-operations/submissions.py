'''
fail to solve
good and classic question
trick to use left_count to represent right count is execellent

'''
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[None] * m for _ in range(m+1) ]   # memorization for dfs
        # ans = -inf
        def dfs(left_count, i): # left elemnt taken, index of multipliers
            if i == m:
                return 0
            if dp[left_count][i] != None:
                return dp[left_count][i]
            
            # right_count = i-left_count
            # right_index = n-right_count-1
            
            right_index = n-(i-left_count)-1
            
            multiplier = multipliers[i]
            
            # max if choose right
            right_max = nums[right_index]*multiplier+dfs(left_count, i+1)
            
            # max if choose left
            left_max = nums[left_count]*multiplier+dfs(left_count+1, i+1)
            
            dp[left_count][i] = max(left_max, right_max)
            
            return dp[left_count][i]
        
        return dfs(0,0)
