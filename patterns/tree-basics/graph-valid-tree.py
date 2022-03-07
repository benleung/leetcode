'''
very basic, but able to finish only after reading solution, should challenge again
'''
from collections import defaultdict
class Solution:
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(list)
        parent = {} # indicate expanded from which node
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        st = [0]
        parent[0] = None # a random 

        while st:
            node = st.pop()
            
            # parent[node] exists here
            
            for neighbor in graph[node]:
                if parent[node] == neighbor:
                    # already visited
                    continue
                if neighbor in parent and parent[neighbor] != node:
                    # a node cannot have multiple parent
                    return False
                
                parent[neighbor] = node
                st.append(neighbor)
        return len(parent) == n

'''
similar ways i did for other graphs
'''

from collections import defaultdict
class Solution:
    W = 0
    G = 1
    B = 2
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        color = defaultdict(lambda: Solution.W)
        graph = defaultdict(list)
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        counter = set([i for i in range(n)])
        explored = set()

        st = [0]
        color[0] = Solution.G
        while st:
            n = st.pop()
            color[n] = Solution.B
            explored.add(n)

            for adj in graph[n]:
                if color[adj] == Solution.G:
                    return False
                if color[adj] == Solution.W:
                    st.append(adj)
                    color[adj] = Solution.G
        
        if counter != explored:
            return False
        
        return True
