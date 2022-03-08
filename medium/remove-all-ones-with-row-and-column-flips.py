'''
15'
intuitive if think about the necessary actions required to reach goal
'''
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        N = len(grid)
        M = len(grid[0])
        
        
        
        # NM
        for i in range(N):
            if grid[i][0] == 1:
                for j in range(1,M):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0
        
        for i in range(1, M):
            for j in range(1, N):
                if grid[j][i] != grid[j-1][i]:
                    return False
        return True
