# 6 min (2nd trial)
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left = 0
        right = len(nums)-1
        
        result = []
        
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                result = [nums[left]**2] + result
                left += 1
            else:
                result = [nums[right]**2] + result
                right -= 1
                
        return result

# 4 min (3rd try in a few weeks)
# <= instead of < is good check
# forget to **2
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = deque()
        
        left = 0
        right = len(nums)-1
        
        while left<=right:
            l = nums[left]**2
            r = nums[right]**2
            if l<=r:
                ans.appendleft(r)
                right -= 1
            else:
                ans.appendleft(l)
                left += 1
                
        
        return list(ans)
