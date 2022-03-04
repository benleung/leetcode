'''
there is Topological Sort in the solution that worth studying
'''

'''
8' detect cyclic only (course-schedule-ii is better)
finish fast because did course-schedule-iiyesterday

good
- return cyclic
'''
from collections import defaultdict
class Solution:
    W = 0
    G = 1
    B = 2
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        color = defaultdict(lambda: Solution.W)
        graph = defaultdict(list)
        
        for a, pre in prerequisites:
            graph[pre].append(a)
        
        def isCyclic(n):
            color[n] = Solution.G
            
            for adj in graph[n]:
                if color[adj] == Solution.G:
                    return True
                if color[adj] == Solution.W:
                    if isCyclic(adj):
                        return True
            
            color[n] = Solution.B
            
        for i in range(numCourses):
            if color[i] == Solution.W:
                if isCyclic(i):
                    return False
        return True
