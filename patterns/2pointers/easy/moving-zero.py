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

'''
slow and fast pointer, about 5', one time pass
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            while fast < len(nums) and nums[fast] == 0:
                fast += 1
            # nums[fast] != 0
            if fast < len(nums):
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        for i in range(slow, len(nums)):
            nums[i] = 0
