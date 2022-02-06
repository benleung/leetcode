class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums)
        delCount = 0
        for i in range(0,l):
            if nums[i-delCount] == val:
                del nums[i-delCount]
                delCount += 1
        return len(nums)