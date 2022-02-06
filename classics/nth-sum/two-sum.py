class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if idx1 != idx2 and num1 + num2 == target:
                    return [idx1, idx2]
# https://leetcode.com/problems/two-sum