'''
has tricky point
30' (think by myself)
'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list) # a->(b, 2)
        for equ, val in zip(equations, values):
            up, down = equ
            graph[up].append((down, val))
            graph[down].append((up, 1.0/val))
        
        print(graph)
        
        ans = []
        visited = set()
        def dfs(cur, node, target): # return True found
            if node == target:
                ans.append(cur)
                return True
            for adj_node, adj_weight in graph[node]:
                if adj_node in visited:
                    continue
                
                visited.add(adj_node)
                if dfs(cur*adj_weight, adj_node, target):
                    return True
                visited.remove(adj_node)
            return False
        for q in queries:
            start, target = q
            
            if start not in graph:
                ans.append(-1) # case of "x","x"
                continue
            visited = {start}
            if not dfs(1, start, target):
                ans.append(-1)
            visited.remove(start)
        return ans
