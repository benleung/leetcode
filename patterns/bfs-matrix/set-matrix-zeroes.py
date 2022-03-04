'''
2' (medium though)
there's also a O(1) space solution that worth looking at
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_with_0 = set()
        cols_with_0 = set()
        
        R = len(matrix)
        C = len(matrix[0])
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    rows_with_0.add(r)
                    cols_with_0.add(c)
                    
        
        for r in range(R):
            for c in range(C):
                if r in rows_with_0 or c in cols_with_0:
                    matrix[r][c] = 0
