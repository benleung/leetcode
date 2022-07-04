'''
bad: fail to think of sol.

to learn:
- from itertools import product
- convert surrounded-region to a counting lake problem
- if converting each elements in-place doesn't matched the desired out, run the for loop again
'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.Y = len(board)
        self.X = len(board[0])
        for y in range(self.Y):
            self.dfs(board, y, 0)
        for y in range(self.Y):
            self.dfs(board, y, self.X-1)
        for x in range(self.X):
            self.dfs(board, 0, x)
        for x in range(self.X):
            self.dfs(board, self.Y-1, x)
        
        for x in range(self.X):
            for y in range(self.Y):
                if board[y][x]  == 'O':
                    board[y][x] = 'X'
                elif board[y][x] == 'E':
                    board[y][x] = 'O'

    def dfs(self, board, y, x): # return True of not captured
        if board[y][x] != 'O':
            return
        board[y][x] = 'E'
        directions = [[-1, 0], [1,0], [0,-1],[0,1]]
        for direction in directions:
            newY = direction[0] + y
            newX = direction[1] + x
            if newY<0 or newY>=self.Y or newX<0 or newX >= self.X:
                continue
            if board[newY][newX] == 'O':
                self.dfs(board, newY, newX)
            
            