'''
20'
interesting and worth retrying
similar to 4 island coloring
'''
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        h = {
            True: set(), # a group
            False: set() # b group
        }
        
        queue = [] # (val, is_a)
        for i in range(len(graph)):
            if i not in h[True] and i not in h[False]:
                queue.append((i, True))
                
            while queue: # all connected island is explored
                val, is_a = queue.pop()
                if val in h[not is_a]:
                    return False
                if val not in h[is_a]:
                    h[is_a].add(val)
                    for adj_val in graph[val]:
                        queue.append((adj_val, not is_a))
                        
                
        return True
