'''
originally thought it is dp
should do again in future
'''
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        
        def heappush(val):
            heapq.heappush(heap, -val)
            
        def heappop():
            return -heapq.heappop(heap)
        
        N = len(heights)
        total_dist = 0
        for i in range(N):
            if i == N-1:
                return i
            dist = max(heights[i+1] - heights[i], 0)  # distance to next
            total_dist += dist
            if dist > 0:
                heappush(dist)
            
            if total_dist > bricks:
                if ladders >0:
                    total_dist -= heappop()
                    ladders -= 1
                else:
                    return i
