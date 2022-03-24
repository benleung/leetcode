'''
3/22 revisit
22'

stuck on 
- dfs ancestor function with exception handling for root

mistake on 
- visited
- if xxx, where xxx can be 0
'''

from collections import defaultdict
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(n)]
        
        graph = defaultdict(list)
        
        
        for parent, child in edges:
            graph[parent].append(child)
        
        visited = set()
        
        # append assign ancestor to each node
        # 
        def dfs(node, ancestor = None):
            if node in visited:
                return
            else:
                visited.add(node)
            
            # append ancestor
            if ancestor != None:
                ans[node].append(ancestor)
            else:
                ancestor = node
            
            # append ancestor to all the children
            for child in graph[node]:
                dfs(child, ancestor)
            
        for i in range(n):
            visited = set()
            dfs(i)
        
        return ans
        
        
    
    