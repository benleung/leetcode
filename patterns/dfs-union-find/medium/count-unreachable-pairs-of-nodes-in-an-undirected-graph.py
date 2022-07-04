'''
20min
'''
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        visited = set()
        groups = []
        def dfs(node):
            visited.add(node)
            groups[-1] += 1
            for adj in graph[node]:
                if adj not in visited:
                    dfs(adj)
        
        for node in range(n):
            if node not in visited:
                groups.append(0)
                dfs(node)
            
        ans = comb(n, 2)
        G = len(groups)
        for group in groups:
            if group >= 2:
                ans -= comb(group, 2)
            
        return ans
