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

'''
O(n)

'''
from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = Counter(nums)
        x, y = -1, -1
        for i in range(len(nums)-1, -1,-1):
            num = nums[i]
            if target - num in h:
                if not (target - num == num and h[num] == 1):
                    x, y = target - num, num
                    return [nums.index(target - num),i]
