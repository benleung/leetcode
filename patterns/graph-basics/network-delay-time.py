'''
revisited on 4/14 (13')
12'
Dijkstra
'''
from collections import defaultdict
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        visited = set()
        shortest_dist = 0
        min_heap = [(0, k)]
        graph = defaultdict(list) # [(dest, weight)]
        
        # build graph
        for src, dest, weight in times:
            graph[src].append((dest, weight))
        
        # Dijkstra algorithm
        while min_heap:
            dist, node = heapq.heappop(min_heap)
            if node in visited:
                # skip node that arrives later
                continue
            visited.add(node)
            shortest_dist = max(shortest_dist, dist)
            
            # explore adj node
            for adj, weight in graph[node]:
                heapq.heappush(min_heap, (dist + weight, adj))
            
        
        return shortest_dist if len(visited) == n else -1
