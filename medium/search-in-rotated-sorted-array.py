
'''
29'(6' to understand q)

good
- calculate mapIndex correct
- know the trick: Compare nums[0] and target to identify in which part one has to look for target


to revise again
- mapIndex correctly for rotated array

'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find pivot
        left  = 0
        right = len(nums)-1
        
        first = nums[0]
        pivot = None
        
        while pivot == None:
            center = (left+right)//2
            
            if first > nums[center]:
                # right part
                if nums[center-1]>nums[center]: # target found
                    pivot = center
                else:
                    right = center - 1
            else:
                # left part
                left = center + 1
            if left>right:
                break
        # rotated back according to pivot
        if pivot != None:
            nums = nums[pivot:] + nums[:pivot]
        
        # norma binary search
        left = 0
        right = len(nums)-1
        while left<=right:
            center = (left+right)//2
            if nums[center]==target:
                return center if pivot is None else self.mapIndex(center,pivot,len(nums))
            elif nums[center]<target:
                left = center+1
            elif nums[center]>target:
                right = center-1
            
            
        return -1
        # edge cases
        # length of 1 -> took care by left>right
        # not foudn
        # no pivot -> took care by left>right
    def mapIndex(self, i, pivot, length):
        if i<length-pivot:
            return i+pivot
        else:
            return i-(length-pivot)
