# 6'46"
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a_rows = defaultdict(int)
        a_cols = defaultdict(int)
        a_posDiag = defaultdict(int)
        a_negDiag = defaultdict(int)
        
        b_rows = defaultdict(int)
        b_cols = defaultdict(int)
        b_posDiag = defaultdict(int)
        b_negDiag = defaultdict(int)
        
        for i, (row, col) in enumerate(moves):
            if i %2 == 0:
                # A
                a_rows[row] += 1
                a_cols[col] += 1
                a_posDiag[row+col] += 1
                a_negDiag[row-col] += 1
                if 3 in [a_rows[row], a_cols[col], a_posDiag[row+col], a_negDiag[row-col]]:
                    return "A"
            else:
                # B
                b_rows[row] += 1
                b_cols[col] += 1
                b_posDiag[row+col] += 1
                b_negDiag[row-col] += 1
                if 3 in [b_rows[row], b_cols[col], b_posDiag[row+col], b_negDiag[row-col]]:
                    return "B"
        else:
            return "Draw" if len(moves) == 9 else "Pending"
