# from math import comb
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0]) 
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        def dp(i,j):
            if i<0 or j<0:
                return 0
            return obstacleGrid[i][j]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = dp(i-1,j) + dp(i,j-1)
        
        return obstacleGrid[m-1][n-1]

'''
math solution doesn't work because of duplicate
'''
# from math import comb
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         ans = comb(m-1+n-1,m-1)
#         for row in range(m):
#             for col in range(n):
#                 if obstacleGrid[row][col] == 1:
#                     obstacle_to_goal_offset_y = m-1-row
#                     obstacle_to_goal_offset_x = n-1-col
#                     ans -= comb(row + col, row) * comb(obstacle_to_goal_offset_y + obstacle_to_goal_offset_x, obstacle_to_goal_offset_y)
        
#         return ans
