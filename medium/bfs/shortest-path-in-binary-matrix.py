# 12' design
# 44' finish coding but TLE
'''
learn
- neighbor element (anki)

'''
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        iMax = len(grid)-1
        jMax = len(grid[0])-1
        
        goal = [iMax, jMax]
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        def getNeighbours(pos):
            for row_difference, col_difference in directions:
                new_row = pos[0] + row_difference
                new_col = pos[1] + col_difference
            
                if not(0 <= new_row <= iMax and 0 <= new_col <= jMax):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield [new_row,new_col]

        if grid[0][0] != 0:
            return -1
        q = deque([[0,0]])
        grid[0][0] = 1
        
        while q:
            pos = q.popleft()

            if pos == goal:
                return grid[pos[0]][pos[1]]
            for i,j in getNeighbours(pos): # skip neighbours that are already read
                q.append([i,j])
                grid[i][j] = grid[pos[0]][pos[1]] +1
        
        return -1 # path not found
