'''
11'

there is faster way to find median (O(n) on average)
should practice later
'''
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        
        median = nums[len(nums)//2] # right centered
        
        ans = 0
        
        for num in nums:
            ans += abs(median - num)
        
        return ans
