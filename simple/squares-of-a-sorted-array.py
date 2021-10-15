# 6 min (2nd trial)
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left = 0
        right = len(nums)-1
        
        result = []
        
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                result = [nums[left]**2] + result
                left += 1
            else:
                result = [nums[right]**2] + result
                right -= 1
                
        return result
