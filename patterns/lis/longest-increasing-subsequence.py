'''
slow solution O(N^2)

however accepted in leetcode

has a smarter solution, revise later
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] *(N)
        dp[N-1] = 1
        for i in range(N-2, -1, -1):
            for j in range(1, N-i):
                if nums[i]<nums[i+j]:
                    dp[i] = max(dp[i], dp[i+j] + 1)
        
        return max(dp)
