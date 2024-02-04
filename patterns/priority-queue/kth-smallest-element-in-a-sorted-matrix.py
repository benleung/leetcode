'''
forget visited
good to solve the problem myself
15'
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        heap = [(matrix[0][0], 0 , 0)]
        visited = set((0,0))
        directions = [(0, 1), (1, 0)]
        
        for _ in range(k-1):
            _, row, col = heapq.heappop(heap)
            
            for dr, dc in directions:
                new_row, new_col = dr+row, dc+col
                if 0<=new_row<N and  0<=new_col<N and (new_row, new_col) not in visited:
                    heapq.heappush(heap, (matrix[new_row][new_col], new_row, new_col))
                    visited.add((new_row, new_col))
        return heap[0][0]
