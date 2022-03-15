'''
30'
'''
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        R = len(maze)
        C = len(maze[0])
        inf = float('inf')
        failed_position = set()
        
        l = [[None] * C for _ in range(R)]
        for r in range(R):
            left_most = inf
            for c in range(C):
                if maze[r][c] == 1:
                    left_most = c + 1
                else:
                    left_most = min(left_most, c)
                    l[r][c] = left_most
        
        right = [[None] * C for _ in range(R)]
        for r in range(R):
            right_most = -inf
            for c in range(C-1, -1, -1):
                if maze[r][c] == 1:
                    right_most = c - 1
                else:
                    right_most = max(right_most, c)
                    right[r][c] = right_most
        
        
        u = [[None] * C for _ in range(R)]
        for c in range(C):
            top_most = inf
            for r in range(R):
                if maze[r][c] == 1:
                    top_most = r + 1
                else:
                    top_most = min(top_most, r)
                    u[r][c] = top_most
        
        d = [[None] * C for _ in range(R)]
        for c in range(C):
            down_most = -inf
            for r in range(R-1, -1, -1):
                if maze[r][c] == 1:
                    down_most = r - 1
                else:
                    down_most = max(down_most, r)
                    d[r][c] = down_most
                    
        self.visited = {(start[0],start[1])}
        def backtrack(r,c):
            if (r,c) in failed_position:
                return False
            
            if r == destination[0] and c == destination[1]:
                return True
            
            candidates = [(u[r][c], c), (d[r][c], c), (r, l[r][c]), (r, right[r][c])]
            for next_try in candidates:
                if next_try not in self.visited:
                    self.visited.add(next_try)
                    if backtrack(next_try[0],next_try[1]):
                        return True
                    self.visited.remove(next_try)
            
            failed_position.add((r,c))
            
            return False
        return backtrack(start[0],start[1])
