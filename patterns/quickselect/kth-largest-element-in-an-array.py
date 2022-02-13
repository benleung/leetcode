'''
a class kth-largest-elemnt logic

good to do the inplace group (2 pointer technique)
  could be faster
edge case programming is a bit slow
no need to hesitate > or >==
'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums)-1, k)
        
        
    def quickSelect(self, nums, l, r, k):
        # pivot = nums[r]
        # if l == k-1:
        #     return nums[l]
        
        # grouping
        fast, slow = l, l
        while fast < r: #last element is pivot, so skip
            if nums[fast] > nums[r]: #hesitate here (decide end of or start of, not effect on ...)
                nums[slow], nums[fast] = nums[fast], nums[slow]
                fast += 1
                slow += 1
            else:
                fast += 1
        nums[slow], nums[r] = nums[r], nums[slow]
        
        if slow == k-1:
            return nums[slow]
        elif slow < k-1:
            return self.quickSelect(nums, slow + 1, r, k)
        else:
            return self.quickSelect(nums, l, slow-1, k)
