'''
15' tried again on 11/23

'''

'''
14'
'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R = len(mat)
        C = len(mat[0])
        q = deque()
        for r in range(R):
            for l in range(C):
                if mat[r][l] == 0:
                    q.append((r,l))
                else: 
                    mat[r][l] = None

        neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            (r, c) = q.popleft()
            for (dr,dc) in neighbours:
                newr,newc = r+dr, c+dc
                if (0<=newr<R and 0<=newc<C) and mat[newr][newc] == None:
                    mat[newr][newc] = mat[r][c] + 1
                    q.append((newr,newc))

        return mat


'''
10'

similar to shortest-path-in-binary-matrix

learn
- initial root not necessary one, could be multiple items for the queue initially
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R = len(mat)
        C = len(mat[0])
        
        visited = set()
        q = deque()
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 0:
                    q.appendleft((r,c,0))
                    visited.add((r,c))
                else:
                    mat[r][c] = float("inf")

        while q:
            (nextR, nextC, depth) = q.pop()
            newDepth = depth + 1
            neighborDiff = [(0,1),(0,-1),(-1,0),(1,0)]
            for (dr, dc) in neighborDiff:
                new = (newR, newC) = (dr+nextR, dc+nextC)
                if 0<=newR<R and 0<=newC<C and new not in visited:
                    mat[newR][newC] = min(mat[newR][newC], newDepth)
                    q.appendleft((newR, newC, newDepth))
                    visited.add(new)

        return mat


'''
30'
time complexity too slow, overtime

learn
- Init deque with tuple
- Visited should be added after adding to queue
- new = (newR, newC) = (dr+nextR, dc+nextC)
- deque((1,2)) -> [1, 2]  (not [(1,2)] )  # cannot init deque with tuple
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans = [[x if x==0 else None for x in row] for row in mat]
        
        R = len(mat)
        C = len(mat[0])
        
        def bfs(r,c):
            visited = set((r,c))
            q = deque()
            q.appendleft((r,c))
            depth = 0
            while q:
                for _ in range(len(q)):
                    (nextR, nextC) = q.pop()
                    if ans[nextR][nextC] == 0:
                        return depth + ans[nextR][nextC]
                    else:
                        neighborDiff = [(0,1),(0,-1),(-1,0),(1,0)]
                        for (dr, dc) in neighborDiff:
                            new = (newR, newC) = (dr+nextR, dc+nextC)
                            if 0<=newR<R and 0<=newC<C and new not in visited:
                                q.appendleft(new)
                                visited.add(new)
                depth += 1
        
        for r in range(R):
            for c in range(C):
                ans[r][c] = bfs(r,c)
        
        return ans
