# solution is here: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/1676610/Python-O(n)-sliding-window-with-2-monotonic-deques-solution-(explanation-included)

'''
O(N^2) TLE
'''
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 1
        
        def isLessThanLimit(a, b):
            return a-b <= limit
        
        for i in range(len(nums)-1):
            curMin = nums[i]
            curMax = nums[i]
            
            for j in range(i+1, len(nums)):
                curMax = max(curMax, nums[j])
                curMin = min(curMin, nums[j])
                if isLessThanLimit(curMax,curMin):
                    ans = max(ans, j-i+1)
                else:
                    break
        
        return ans
