
'''
12'

bad
- mistake on didn't check "if oldColor == newColor"

learn ( from bad)
dfs always require a mechanism to avoid revisiting the same node
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        M = len(image)
        N = len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image

        def dfs(r,c):
            if not (0<=r<M and 0<=c<N):
                return
            if image[r][c] != oldColor:
                return
            
            image[r][c] = newColor
            neighborDiff = [[1,0],[-1,0],[0,-1],[0,1]]
            for diff in neighborDiff:
                dfs(r+diff[0],c+diff[1])
            
        
        dfs(sr, sc)
        
        return image
