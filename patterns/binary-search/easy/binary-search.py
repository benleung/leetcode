'''
6'27"

fast engouh, can be a bit faster in typing only
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums = nums
        return self.binarySearch(0, len(nums)-1, target)
        
    def binarySearch(self, left, right, target):
        if left > right:
            return -1

        leftCenter = (left + right)//2
        num = self.nums[leftCenter]
        if num == target:
            return leftCenter
        elif num > target:
            return self.binarySearch(left, leftCenter -1, target)
        elif num < target:
            return self.binarySearch(leftCenter + 1, right, target)
