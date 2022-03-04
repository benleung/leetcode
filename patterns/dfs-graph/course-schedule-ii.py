'''
21' after knowing the ans in advance
'''
from collections import defaultdict
class Solution:
    WHITE = 0
    GRAY = 1
    BLACK = 2
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        color = defaultdict(lambda: Solution.WHITE)
        stack = []
        self.isCycle = False
        
        for a, b in prerequisites:
            graph[b].append(a)
        
        def dfs(n):
            if self.isCycle:
                return
            
            color[n] = Solution.GRAY
            for adj_node in graph[n]:
                if color[adj_node] == Solution.GRAY:
                    self.isCycle = True
                    return
                if color[adj_node] == Solution.WHITE:
                    dfs(adj_node)
            
            stack.append(n)
            color[n] = Solution.BLACK
            
        for i in range(numCourses):
            if color[i] == Solution.WHITE:
                dfs(i)
                if self.isCycle:
                    return []
        
        return stack[::-1]

'''
failed because insufficient knowledge about cyclic graph
'''

from collections import defaultdict
class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list) # a->b a should start before b
        color = defaultdict(lambda: Solution.WHITE)
        ans = deque()
        self.isPossible = True
        
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
        
        def dfs(node):
            if not self.isPossible:
                return
            color[node] = Solution.GRAY
            for adj in graph[node]:
                if color[adj] == Solution.GRAY:
                    self.isPossible = False
                    return
                if color[adj] == Solution.WHITE:
                    dfs(adj)
            color[node] = Solution.BLACK
            ans.appendleft(node)
            
        
        for i in range(numCourses):
            if color[i] == Solution.WHITE:
                dfs(i)
        
        if not self.isPossible:
            return []
        
        return ans
