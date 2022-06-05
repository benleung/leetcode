'''
partition an array into two
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        slow = 0
        for i, num in enumerate(nums):
            nums[slow], nums[i] = nums[i], nums[slow]
            if num % 2 == 0:
                slow += 1
        return nums
