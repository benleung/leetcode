'''
5'
'''

from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        h = Counter(nums)
        accSum = 0
        j = 0
        for i in range(0,3):
            accSum += h[i]
            while j < accSum:
                nums[j] = i
                j += 1
