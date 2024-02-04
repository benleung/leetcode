'''
17' -> 11'

so typical, luckily i did 01-matrix before, such that know should define multiple q
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()  # (row,column)
        q = deque()  #(row,column)
        depth = 0
        
        R = len(grid)
        C = len(grid[0])
        for r in range(R):
            for c in range(C):
                target = grid[r][c]
                if target == 1:
                    fresh.add((r,c))
                elif target == 2:
                    q.appendleft((r,c))
        
        neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
        # lastFreshLength = len(fresh) # probably not necessary
        while q and len(fresh)>0:
            for _ in range(len(q)):
                (r,c) = q.pop()
                for (rDiff, cDiff) in neighbors:
                    (newR, newC) = (r+rDiff,c+cDiff)
                    if (newR,newC) in fresh:  # 0<=newR<R and 0<=newC<C and 
                        q.appendleft((newR,newC))
                        fresh.remove((newR,newC))
                        
                
            depth += 1
        return depth if len(fresh) == 0 else -1
