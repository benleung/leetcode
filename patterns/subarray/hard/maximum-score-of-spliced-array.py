'''
25'
'''
class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:  
        
        ans = 0
        
        # move value to nums1
        total_diff = sum(nums1)-sum(nums2)
        N = len(nums1)
        
        diffs = [num2-num1 for num1, num2 in zip(nums1, nums2)]
        
        prefix_sum = 0 
        min_prefix_sum = 0
        max_prefix_sum = 0
        for diff in diffs:
            prefix_sum+=diff
            max_prefix_sum = max(max_prefix_sum, prefix_sum-min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
        
        ans = max(ans, max_prefix_sum + sum(nums1))

        # move value to nums2
        total_diff = sum(nums2)-sum(nums1)
        N = len(nums1)
        
        diffs = [num1-num2 for num1, num2 in zip(nums1, nums2)]
        
        
        
        prefix_sum = 0 
        min_prefix_sum = 0
        max_prefix_sum = 0
        for diff in diffs:
            prefix_sum+=diff
            max_prefix_sum = max(max_prefix_sum, prefix_sum-min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
        
        ans = max(ans, max_prefix_sum + sum(nums2))

        return ans
