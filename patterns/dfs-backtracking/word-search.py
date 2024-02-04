'''
revisited on 12/12
23'
'''

'''
revisited on 2/24
34'
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Y = len(board)
        X = len(board[0])
        
        neighbours = [(0,1),(0,-1),(-1,0),(1,0)]
        self.visited = set() # coordinates
        
        def backtrack(i, target):
            (y, x) = target
            if not (0<=y<Y and 0<=x<X):
                # out of bound
                return False
            
            if board[y][x] != word[i]: # impossible to out of bount
                # the candidate fails
                return False
            
            if i == len(word) - 1:
                # reach the end so final result
                return board[y][x] == word[i]

            self.visited.add(target)
            for (dy, dx) in neighbours:
                newTarget = (y + dy, x+dx)
            
                i += 1
                if backtrack(i, newTarget):
                    return True
                i -= 1
            self.visited.remove(target)
            return False
                
            
        for y in range(Y):
            for x in range(X):
                target = (y,x)
                if backtrack(0,target):
                    return True
            
        return False


'''
38'

bad
- forget return after transversing all neighbours

good
- success without too many fail attempts

learn
- backtrack that return True/False
- neighbour
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Y = len(board)
        X = len(board[0])
        visited = [[False]*X for _ in range(Y) ]

        def neighbours(x, y):
            diff = [
                (-1,0),(1,0),(0,-1),(0,1)
            ]
            
            for (dx,dy) in diff:
                newX = x + dx
                newY = y + dy
                if 0<=newX<X and 0<=newY<Y and not visited[newY][newX]:
                    yield (newX,newY)

        def backtrack(depth, candidate): # cadidate: (X, Y)
            (x,y)=candidate
            # fail the candidate
            if board[y][x] != word[depth]:
                return False
            
            depth += 1
            
            # new candidate is accepted
            if depth == len(word):
                return True
            
            for (newX, newY) in neighbours(x, y):
                visited[y][x] = True
                res = backtrack(depth, (newX,newY))
                visited[y][x] = False
                if res:
                    return True
            return False
        
        
        for y in range(Y):
            for x in range(X):
                visited[y][x] = True
                res = backtrack(0, (x, y))
                visited[y][x] = False
                if res:
                    return True
        return False



'''
solution in leetcode

- modify the board in place to save place

'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False


    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret: break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return ret
