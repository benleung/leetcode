'''
19'
should create get_number and set_number to simplify
'''
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R = len(grid)
        C = len(grid[0])
        k %= R*C
        
        def set_number(i, val):
            r = i//C
            c = i%C
            
            grid[r][c] = val
            
        def get_number(i):
            r = i//C
            c = i%C
            
            return grid[r][c]
        
        if k == 0:
            return grid
        
        
        temp = deque()
        for i in range(R*C-k,R*C):
            temp.append(get_number(i))
        for i in range(R*C):
            val = temp.popleft()
            temp.append(get_number(i))
            set_number(i, val)
        return grid
