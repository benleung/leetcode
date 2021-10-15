class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = -101
        deletedCount = 0
        l = len(nums)
        for index in range(0, l):
            if cur != nums[index-deletedCount]:
                cur = nums[index-deletedCount]
            else:
                del nums[index - deletedCount]
                deletedCount += 1
                
        return len(nums)
