'''
6'
revisited on 12/11: 9'
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        self.currArea = 0
        R = len(grid)
        C = len(grid[0])
        
        
        def dfs(r,c):
            if not(0<=r<R and 0<=c<C) or grid[r][c] == 0:
                return
            grid[r][c] = 0
            self.currArea += 1
            neighbours = [[0,-1],[0,1],[-1,0],[1,0]]
            for neighbour in neighbours:
                [newR,newC] = [r+neighbour[0], c+neighbour[1]]
                dfs(newR,newC)
            
        for c in range(C):
            for r in range(R):
                dfs(r,c)
                maxArea = max(maxArea, self.currArea)
                self.currArea = 0
        
            
        
        return maxArea
