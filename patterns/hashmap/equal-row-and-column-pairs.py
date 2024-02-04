'''
technique to hash a long array
-> convert array to a string

use tuple(x) is a smarting solution
'''
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        h = defaultdict(int)
        N = len(grid)
        for col in range(N):
            col_str = []
            for row in range(N):
                col_str.append(str(grid[row][col]))
            h[",".join(col_str)] += 1
        
        ans = 0
        for cols in grid:
            key = ",".join(map(str, cols))
            ans += h[key]
        return ans
