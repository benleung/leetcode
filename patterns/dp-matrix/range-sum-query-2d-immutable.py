
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.dp = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            rowSum = 0
            for col in range(cols):
                rowSum += matrix[row][col]
                self.dp[row][col] = self.dp_func(row-1, col) + rowSum
        
    def dp_func(self, row, col):
        if row <0 or col <0:
            return 0
        return self.dp[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
            
        return self.dp_func(row2, col2) - self.dp_func(row2, col1-1) - self.dp_func(row1-1, col2) + self.dp_func(row1-1, col1-1)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
