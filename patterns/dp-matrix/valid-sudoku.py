'''
11'
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        regions = [set() for _ in range(9)]
        
        def find_region(row, col):
            region_col = col // 3
            region_row = row // 3
            return regions[3*region_row + region_col]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                cell = board[row][col]
                region = find_region(row, col)
                if cell == ".":
                    continue
                if cell in rows[row] or cell in cols[col] or cell in region:
                    return False
                
                rows[row].add(cell)
                cols[col].add(cell)
                region.add(cell)

        return True
