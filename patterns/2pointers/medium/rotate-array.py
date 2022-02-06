# 25 min -> 5min
# Approach 2: Using Extra Array is used here
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        step = k % l # 0~l-1
        nums[:] = nums[-step:] + nums[:l-step] if step != 0 else nums
