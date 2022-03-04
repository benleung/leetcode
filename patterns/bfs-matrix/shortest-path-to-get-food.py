'''
29' with whiteboarding

bad
wasted time on bug (dun rewrite the goal)
return the goal when searching in neighbor is actually easier (no need to be afraid of rewriting the goal)
visit right after apppending to queue/stack
'''
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
            
        def find_my_location(): # return: (r, c)
            for r in range(R):
                for c in range(C):
                    if grid[r][c] == "*":
                        return (r,c)
        
        def canExplore(r,c):
            if not (0<=r<R) or not (0<=c<C):
                return False
            return grid[r][c] == "O" or grid[r][c] == "#"
        
        r, c = find_my_location()
        
        q = deque() # [(r, c, step)]  # append -> popleft()
        
        q.append((r,c,0))
        grid[r][c] = "X"
        
        while q:
            r, c, step = q.popleft()
            if grid[r][c] == "#":
                return step
            
            # explore neighbours
            neighbours = [
                (-1,0),
                (1,0),
                (0,1),
                (0,-1),
            ]
            
            for dr, dc in neighbours:
                new_r, new_c = r + dr, c + dc
                if canExplore(new_r,new_c):
                    q.append((new_r, new_c, step + 1))
                    if grid[new_r][new_c] == "O":
                        grid[new_r][new_c] = "X" # here had bug
            
            
        return -1
