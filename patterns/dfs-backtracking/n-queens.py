''''
15'
'''
class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        cols = set()
        posDiag = set() # r+c
        negDiag = set() # r-c
        candidate = [] # columns, final n queens placed
        
        def append_to_ans(ans, candidate):
            combination = []
            for col in candidate:
                row = []
                for i in range(n):
                    row.append("." if i!=col else "Q")
                combination.append("".join(row))
            ans.append(combination)
        
        def backtrack(row):
            if row >= n:
                append_to_ans(ans, candidate)
            for col in range(n):
                if col in cols or row+col in posDiag or row-col in negDiag:
                    continue
                
                cols.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)
                candidate.append(col)
                backtrack(row+1)
                candidate.pop()
                cols.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)
            
        backtrack(0)
        
        return ans
