# slow approach ( 15min)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        for i in reversed(xrange(0, len(nums)-1)):
            if nums[i] == 0:
                for j in range(i, len(nums)-1):
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
