'''
20'
variation of Dijkstra's Algorithm 
'''
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, 0, 0)] # (dist, row, col)
        visited = set() # (row,col)
        
        R = len(heights)
        C = len(heights[0])
        
        curMax = 0
        
        def findNeighbours(row,col): # [(r,c)]
            diff = [(-1,0),(1,0),(0,-1),(0,1)]
            result = []
            for dr, dc in diff:
                r = dr+row
                c = dc+col
                if not (0<=r<R and 0<=c<C):
                    continue
                if (r,c) in visited:
                    continue
                result.append((r,c))
            return result

        while True:
            (dist, row, col) = heapq.heappop(heap)
            visited.add((row,col)) # careless here, should be be careful
            curMax = max(curMax, dist)
            if (row, col) == (R-1, C-1):
                return curMax
            curHeight = heights[row][col]
            for adj_r, adj_c in findNeighbours(row,col):
                adj_height = heights[adj_r][adj_c]
                adj_dist = abs(adj_height - curHeight)
                heapq.heappush(heap, (adj_dist, adj_r, adj_c))
