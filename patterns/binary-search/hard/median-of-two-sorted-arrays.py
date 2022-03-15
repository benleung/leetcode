'''
when O(logn) is needed, binary search is needed
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        # nums1 now has smaller length
        # some elements in nums2 must be used for left partition
        
        total = len(nums2) + len(nums1)
        half = (total) // 2
        isOdd = (total) % 2
        
        left= 0
        right = len(nums1) -1 
        while True:
            
            i = (left+right)//2
            j = half -i -2
            
            left_large_1 = nums1[i] if i >= 0 else float("-inf")
            right_small_1 = nums1[i+1] if i+1 < len(nums1) else float("inf")
            left_large_2 = nums2[j] if j >= 0 else float("-inf")
            right_small_2 = nums2[j+1] if j+1 < len(nums2) else float("inf")
            
            if left_large_1 <= right_small_2 and left_large_2 <= right_small_1:
                if isOdd:
                    return min(right_small_1, right_small_2)
                else:
                    return (max(left_large_1, left_large_2) + min(right_small_1, right_small_2))/2
            elif left_large_1 > right_small_2:
                right = i - 1
            else: # left_large_2 > right_small_1
                left = i + 1
                