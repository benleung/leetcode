'''
some similar thought to surrounded-regions
20'

careless
- used c instead of newC
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R = len(heights)
        C = len(heights[0])
        
        po = [[False] * C for _ in range(R)]
        ao = [[False] * C for _ in range(R)]
        
        ans = []
        
        def dfs(r, c, ocean):
            ocean[r][c] = True
            neighbors= [
                [0,-1],
                [0,1],
                [-1,0],
                [1,0],
            ]
            for dr, dc in neighbors:
                newR, newC = dr+r, dc + c
                if not (0<=newR<R) or not (0<=newC<C):
                    continue # out of boundry
                
                if ocean[newR][newC]:
                    continue # duplicate, skip
                
                if heights[newR][newC] >= heights[r][c]:
                    dfs(newR,newC,ocean)
         
        # alantic ocean
        r = R-1
        for c in range(C):
            if not ao[r][c]: # not visited
                dfs(r,c, ao)
        c = C -  1
        for r in range(R):
            if not ao[r][c]: # not visited
                dfs(r,c, ao)
        
        # pacifici ocean
        r = 0
        for c in range(C):
            if not po[r][c]: # not visited
                dfs(r,c, po)
        c = 0
        for r in range(R):
            if not po[r][c]: # not visited
                dfs(r,c, po)
        
        
        # ans
        for r in range(R):
            for c in range(C):
                if po[r][c] and ao[r][c]:
                    ans.append([r,c])
        return ans
