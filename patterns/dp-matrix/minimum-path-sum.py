'''
15' dp
whiteboarding so spent some time

'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        d = [[float('inf')] *(N+1) for _ in range(M+1)]
        
        for i in range(1,M+1):
            for j in range(1,N+1):
                if i == 1 and j == 1:
                    d[i][j] = grid[i-1][j-1]
                else:
                    d[i][j] = min( d[i-1][j]+grid[i-1][j-1], d[i][j-1]+grid[i-1][j-1] )
        return d[M][N]
