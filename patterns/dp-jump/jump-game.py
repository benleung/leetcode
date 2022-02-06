'''
good to think of the bottom-up dp solution myself

learn:
- think about the near end of jumping
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [True]*N
        # dp[N-2] = nums[N-2]
        for i in range(N-2, -1, -1):
            maxStep = nums[i]
            dp[i] = True in dp[i+1:i+1+maxStep]
        return dp[0]
