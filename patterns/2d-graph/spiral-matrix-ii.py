'''
x,y / row/column easy to mixed up
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        h_lo, h_hi, v_lo, v_hi = 0, n-1, 1, n-1
        matrix = [[0]*n for _ in range(n)]
        i = 0
        j = 0
        
        state = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]
        
        statePointer = 0
        cur = 1
        (di, dj) = state[statePointer%4]
        
        while cur <= n**2:
            matrix[i][j] = cur
            cur += 1
            if dj > 0 and j == h_hi:
                h_hi -= 1
                statePointer += 1
            elif dj < 0 and j == h_lo:
                h_lo += 1
                statePointer += 1
            elif di < 0 and i == v_lo:
                v_lo += 1
                statePointer += 1
            elif di > 0 and i == v_hi:
                v_hi -= 1
                statePointer += 1
            (di, dj) = state[statePointer%4]
            i, j = di+i, dj+j
            
        return matrix
