'''
revisited on 3/8
22'
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        total //= 2
        N = len(nums)
        dp = [[False] * (total+1) for _ in range(N+1)]
        for i in range(N+1):
            dp[i][0] = True
        
        for i, num in enumerate(nums):
            for j in range(1, total+1):
                if dp[i][j]: # forgot
                    dp[i+1][j] = True
                if j - num >= 0 and dp[i][j-num]:
                    dp[i+1][j] = True

        return dp[N][total]

'''
revisited on 2/25
20'
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        subsetSum = sum(nums)
        if subsetSum%2 == 1:
            return False
        subsetSum //= 2
        N = len(nums)
        dp = [[False]*(subsetSum+1) for _ in range(N+1)]
        dp[0][0] = True
        
        for i in range(1, N+1):
            for j in range(subsetSum+1):
                dp[i][j] = dp[i-1][j] or (j >= nums[i-1] and dp[i-1][j-nums[i-1]])
        
        return dp[N][subsetSum]

'''

learn
- all cominbations of sum that can be generated from a list
  - for num in nums: for x in dp.copy():
- dp.copy() to avoid the problem of dp being changed while iterating
- partition means all the elements are used
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2 == 1:
            return False
        
        dp = set({0})
        
        for num in nums:
            for x in dp.copy():
                total = x + num
                dp.add(total)
        
        
        return sum(nums) // 2 in dp
