'''
15'
'''

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        ans = 0
        
        height = 0
        width = 0
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        for i in range(len(verticalCuts)):
            width = max(verticalCuts[i] - (verticalCuts[i-1] if i-1>=0 else 0) , width)
        else:
            width = max(w - verticalCuts[-1], width)
        
        for i in range(len(horizontalCuts)):
            height = max(horizontalCuts[i] - (horizontalCuts[i-1] if i-1>=0 else 0) , height)
        else:
            height = max(h - horizontalCuts[-1], height)

        return height*width % (10**9+7)
