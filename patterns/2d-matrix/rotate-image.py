
'''
upper bound and lower bound for i, j is tricky
for rotating , need to transverse 1/2 of the total choices, which shuldn't overlap
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range((N-1)//2 + 1):
            for j in range(N//2): # tricky
                matrix[i][j], matrix[j][N-i-1],matrix[N-i-1][N-j-1],matrix[N-j-1][i] = matrix[N-j-1][i], matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1]
