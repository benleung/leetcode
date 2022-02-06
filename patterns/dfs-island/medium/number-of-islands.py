'''
13' 

good
- able write the edge cases for 2-d array well

learn
- learn how to solve without hint
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    num += 1
                    self.dfs(grid, i, j)
        return num   
                
    def dfs(self, grid, i, j):
        if grid[i][j] == "1":
            grid[i][j] = "0"
            
            # 4 directions
            if i>=1:
                self.dfs(grid, i - 1, j)
            if i<=len(grid)-2:
                self.dfs(grid, i + 1, j)
            if j>=1:
                self.dfs(grid, i, j - 1)
            if j<=len(grid[i])-2:
                self.dfs(grid, i, j + 1)
