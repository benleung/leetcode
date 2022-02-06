
'''
technique: use visited = Set()
'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        self.ans = 0
        N = len(isConnected[0]) # number of nodes
        for i in range(N):
            self.dfs(i, isConnected, visited)
        return self.ans

    def dfs(self, n, isConnected, visited):
        if n in visited:
            return
        
        # increment number of provinces for discovering an unvisited node
        self.ans += 1
        stack = [n]
        
        # marked all connected nodes as visited
        while stack != []:
            x = stack.pop()
            visited.add(x)
            
            # find connected nodes
            for i,v in enumerate(isConnected[x]):
                if v == 1 and i not in visited:
                    stack.append(i)
