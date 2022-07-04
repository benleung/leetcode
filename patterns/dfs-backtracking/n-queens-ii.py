class Solution:
    def totalNQueens(self, n: int) -> int:
        
        cols = set()
        posDialog = set()
        negDialog = set()
        
        self.count = 0
        
        def backtrack(row):
            if row == n:
                self.count += 1
                return
            
            for col in range(n):
                if col in cols or row+col in posDialog or row-col in negDialog:
                    continue
                    
                add_to_set(row, col)
                backtrack(row+1)
                remove_from_set(row, col)
        
        def add_to_set(row, col):
            cols.add(col)
            posDialog.add(row+col)
            negDialog.add(row-col)
        
        def remove_from_set(row, col):
            cols.remove(col)
            posDialog.remove(row+col)
            negDialog.remove(row-col)
        
        backtrack(0)
        
        return self.count
