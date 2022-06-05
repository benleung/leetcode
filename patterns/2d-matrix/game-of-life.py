'''
18'
some careless mistake
followup 2 is deep:
instead of using 2-d array, using dictinary to represent might be a good solution
to infite board
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 2: 1->0
        # 3: 0->1
        
        R = len(board)
        C = len(board[0])
        def count_neighbors(row, col):
            neighbors = [
                (-1,-1),
                (-1,0),
                (-1,1),
                (0,-1),
                (0,1),
                (1,-1),
                (1,0),
                (1,1),
            ]
            count = 0
            for drow, dcol in neighbors:
                new_row, new_col = drow + row, dcol + col
                if not (0<=new_row<R and 0<=new_col<C):
                    continue
                if board[new_row][new_col] in [1,2]: # original living
                    count += 1
            return count
            
        for row in range(R):
            for col in range(C):
                count = count_neighbors(row, col)
                if board[row][col] == 1 and (count <2 or count>3):
                    board[row][col] = 2
                elif board[row][col] == 0 and count == 3:
                    board[row][col] = 3
        
        for row in range(R):
            for col in range(C):
                count = count_neighbors(row, col)
                if board[row][col] ==2:
                    board[row][col] = 0
                elif board[row][col] ==3:
                    board[row][col] = 1
