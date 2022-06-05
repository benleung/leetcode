'''
14'
good questions, proud of myself AC in this high speed in first run
'''
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        
        # create a graph
        graph = defaultdict(list) # 0 -> [3,2]
        for src, dest in pairs:
            graph[src].append(dest)
            graph[dest].append(src)
        
        # def dfs and assign h
        h = {}  # 0 -> ['a','b','c']
        def dfs(i, heap):
            if i in h:
                # visited
                return
            h[i] = heap
            heapq.heappush(heap, s[i])
            for adj in graph[i]:
                dfs(adj, heap)
            
                
        for i in range(N):
            if i not in h:
                heap = []
                dfs(i, heap)
        
        # iterate 0 to len(s)-1
        ans = []
        for i in range(N):
            ans.append(heapq.heappop(h[i]))
        return "".join(ans)
