'''
revisited on 3/23
6' to finish
'''

'''
revisited 2/24
8'30"

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        ans = 0
        
        left= 0
        right = len(height)-1
        
        while left < right:
            area  = min(height[left],height[right])*(right-left)
            ans = max(area, ans)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        
        return ans
'''

'''
bad
- failed once

good
- make use of 2 pointers technique

learn
- case of ==, not necessary move both
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        ans = 0
        
        left = 0
        right = len(height) - 1
        
        while left < right:
            ans = max(ans, (right-left)*min(height[left],height[right]))
            if height[left] <= height[right]: # separating for ans = ...  is simiplier/better, good here
                left += 1
            else:
                right -= 1
            # if height[left] < height[right]:
            #     left += 1
            # if height[left] > height[right]:
            #     right -= 1
            # if height[left] == height[right]:   # this is the mistake (no need to move both)
            #     right -= 1
            #     left += 1
        
        return ans


'''
7'
brute force
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left = 0
        # right = 1
        ans = 0
        for left in range(0, len(height)-1):
            for right in range(left+1, len(height)):
                area = (right-left)*min(height[left], height[right])
                ans  =max(ans, area)
        
        return ans
