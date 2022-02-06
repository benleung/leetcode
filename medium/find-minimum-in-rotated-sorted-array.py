'''
17'

good
- can realize the trick of (left+right+1)//2 for center
'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        p = None
        while p is None:
            center  = (left+right+1)//2
            
            if center == 0:
                p = 0
                break
            
            if nums[center] < nums[center-1]:
                p = center
            else:
                if nums[0]>nums[center]:
                    right = center - 1
                else:
                    left = center + 1
            if left>right:
                p = 0 # not rotated
        return nums[p]
