'''
1 hr
should have smarter way to start from bottom-left:

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        X = len(matrix)
        Y = len(matrix[0])
        
        
        def helper(lo, hi):
            (lo_x, lo_y) = lo
            (hi_x, hi_y) = hi

            if not (0<=lo_x<=hi_x<X and 0<=lo_y<=hi_y<Y):
                return False
            
            if target < matrix[lo_x][lo_y] or target > matrix[hi_x][hi_y]:
                return False
            
            (centerX, centerY) = ((lo_x+hi_x)//2,(lo_y+hi_y)//2)
            if matrix[centerX][centerY] == target:
                return True
            elif matrix[centerX][centerY] > target:
                return helper((lo_x,centerY), (centerX-1,hi_y)) or helper((lo_x,lo_y), (hi_x,centerY-1))
            else:
                return helper((centerX+1,lo_y), (hi_x,centerY)) or helper((lo_x,centerY+1), (hi_x,hi_y))
            
        return helper((0,0), (X-1, Y-1))
        
    