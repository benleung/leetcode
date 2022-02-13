'''
37'
recursion, slow (5%)

learn
- use product more fluently
- 3-d array
- use all more fluently
- write border check faster (good for anki)

techniques
- +1 by judging from neighbors
'''
from itertools import product

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        maxWidth = max(M,N)
        self.d = [[False] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                self.d[i][j] = matrix[i][j] == "1"
        for length in range(1, maxWidth+1):
            for (i,j) in product(range(M-length+1),range(N-length+1)):
                if self.dp(i,j,length):
                    break  # ok
            else:
                return (length-1)**2
        return maxWidth**2
        
    def dp(self,x, y, length):
        if length == 1:
            return self.d[x][y]
        
        def isBorderAll1():
            return all([self.d[x+length-1][j] for j in range(y, y + length)]) and \
            all([self.d[j][y+length-1] for j in range(x, x + length)])
        
        return self.dp(x, y, length-1) and isBorderAll1()

'''
learn 
- practiced all()
- neighbour
- max value in 2d array
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M = len(matrix)
        N = len(matrix[0])

        neighbors = [ (-1,-1), (-1, 0), (0, -1) ]
        
        for i in range(M):
            for j in range(N):
                matrix[i][j] = int(matrix[i][j])

        for i in range(1,M):
            for j in range(1,N):
                if matrix[i][j] != 0 and all([matrix[i+m][j+n] != 0 for (m, n) in neighbors]):
                    matrix[i][j] = min([matrix[i+m][j+n] for (m, n) in neighbors]) + 1
        return max([max(row) for row in matrix])**2
