'''
27'
binary search can be applied to unsorted array, 
as long as you know which direction (left, right) the solution at each condition check

learning
- hesitate about the case where both left and right neighbor is larger, which direction should i take
- however, the question said we only need to return any of the peaks, 
- so we should check one of the neighbour only, but not both
- O(log2(n)) because reduce the search space in half at every step

'''
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        
        
        
        while True:
            center = (left+right)//2
            
            if (center==0 or nums[center-1] < nums[center]) and (center==len(nums)-1 or nums[center] > nums[center+1]):
                return center # edge case taken care here already: list of 1
            
            # peak on right side is possible
            if nums[center] < nums[center+1]:
                left = center + 1
            else:
                right = center - 1
