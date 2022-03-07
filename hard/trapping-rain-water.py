'''
9'
'''
from collections import defaultdict
class Solution:
    def trap(self, height: List[int]) -> int:
        right = defaultdict(int)
        left = defaultdict(int)
        H = len(height)
        ans = 0
        
        curMax = 0
        for i in range(H-1, -1, -1):
            right[i] = curMax
            curMax = max(height[i], curMax)
        curMax = 0
        for i in range(H):
            left[i] = curMax
            curMax = max(height[i], curMax)
        
        for i in range(H):
            min_of_2sides = min(left[i], right[i])
            ans += max(0, min_of_2sides - height[i])
        
        return ans
