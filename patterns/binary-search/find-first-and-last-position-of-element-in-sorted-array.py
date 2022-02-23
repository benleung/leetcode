'''
16'30"

good 
- fast


bad
- careless to miss out edge case of no length
- forget to reset left/right
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # find lower
        left = 0
        right = len(nums) -1

        lowerEnd = None
        
        if nums == []:
            return [-1,-1]
        
        while lowerEnd == None:
            center = (left+right)//2
            if nums[center] == target:
                if center - 1 < 0 or nums[center - 1] != target:
                    lowerEnd = center
                else:
                    right = center - 1
            elif nums[center] > target:
                right = center - 1
            elif nums[center] < target:
                left = center +1
            
            if left>right:
                lowerEnd = - 1
                
        # find upper
        left = 0
        right = len(nums) -1
        upperEnd = None
        
        while upperEnd == None:
            center = (left+right)//2
            if nums[center] == target:
                if center + 1 >= len(nums) or nums[center + 1] != target:
                    upperEnd = center
                else:
                    left = center + 1
            elif nums[center] > target:
                right = center - 1
            elif nums[center] < target:
                left = center +1
            
            if left>right:
                upperEnd = - 1

        return [lowerEnd, upperEnd]
