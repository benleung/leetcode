class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        minimum = 0
        maximum = len(nums) - 1

        while True:
            if target > nums[maximum]:
                return maximum+1
            if target < nums[minimum]:
                return minimum
            
            middle  = int((maximum+minimum)/2)
            if nums[middle] == target:
                return middle
            if target > nums[middle]:
                minimum = middle+1
            else:
                maximum = middle-1