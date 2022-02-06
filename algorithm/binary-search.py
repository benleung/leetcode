# 10 min
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        min_index = 0
        max_index = len(nums)-1
        
        while True:
            center_index = int((min_index+max_index+1)/2)
            center_val = nums[center_index]
            if center_val == target:
                return center_index
            elif center_val > target:
                max_index = center_index - 1
            elif center_val < target:
                min_index = center_index + 1
            
            if min_index > max_index:
                return -1
