'''
5'
same as number of island, but in graph
'''
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        count = 0
        graph = defaultdict(list)
        
        # build graph
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        def dfs(n):
            visited.add(n)
            for adj in graph[n]:
                if adj not in visited:
                    dfs(adj)
        
        
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
            
        return count
