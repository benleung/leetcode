'''
easy
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0]*N
        for i in range(N-2, -1, -1):
            step = nums[i]
            dp[i] = min(dp[i+1:i+1+step]) + 1 if step >0 else float('inf')
        return dp[0]
