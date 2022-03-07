'''
16'

figure out a medium question without effort

bad:
forget diaganal
'''
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        
        
        # self.rows[1]: player 1, self.rows[2]: player2
        self.rows = [[0]*n for _ in range(3)]
        self.columns = [[0]*n for _ in range(3)]
        self.topleft = [0]*3 # from top-left to bottom-right
        self.bottomleft = [0]*3

    def move(self, row: int, col: int, player: int) -> int:
        self.rows[player][row] += 1
        self.columns[player][col] += 1
        if row == col:
            self.topleft[player] += 1
        if row + col == self.n-1:
            self.bottomleft[player] += 1
        
        if self.rows[player][row] == self.n or self.columns[player][col] == self.n or self.bottomleft[player] == self.n or self.topleft[player] == self.n:
            return player
        else:
            return 0
