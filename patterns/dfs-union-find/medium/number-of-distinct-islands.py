'''
20'

learn
- possible to convert an array (more than 2 elements) into tuple for hashing
- for actions to take for each island, dun do it' instead the dfs function, but do it outside just after calling dfs function instead
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.seen = set()  # in ((r1,c1),(r2,c2), ....) format
        self.candidate = [] # relative coordinate to origin_r, origin_c, in [(r,c)] format
        R = len(grid)
        C = len(grid[0])
        
        def dfs(r,c, origin_r, origin_c):
            # reject coordinate that doesn't work
            if not (0<=r<R and 0<=c<C):
                return
            if grid[r][c]==0:
                return
            
            # indicate this cell is visited
            grid[r][c]=0 
            
            # add current coordinate to self.candidate
            self.candidate.append((r-origin_r,c-origin_c))
            
            # dfs neighbour
            offsets = [(0,1),(0,-1),(1,0),(-1,0)]
            for dy, dx in offsets:
                dfs(r+dy, c+dx, origin_r, origin_c)
            
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    dfs(r,c, r,c)
                    self.seen.add(tuple(self.candidate))
                    self.candidate = []
        
        # print(self.seen)
        
        return len(self.seen)
