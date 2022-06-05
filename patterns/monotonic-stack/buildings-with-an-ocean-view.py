'''
4'22"
easy medium
'''
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        highest = 0
        ans = deque()
        N = len(heights)
        for i in range(N-1,-1,-1):
            height = heights[i]
            if height > highest:
                highest = height
                ans.appendleft(i)
        return ans
