'''
not familiar with heap
'''
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = [] # -dist
        for i in range(k):
            dist = points[i][0]**2 + points[i][1]**2
            heapq.heappush(maxheap, (-dist, i))
        
        for i in range(k, len(points)):
            dist = points[i][0]**2 + points[i][1]**2
            heapq.heappushpop(maxheap, (-dist, i))
        
        return [points[i] for (_, i) in maxheap]

'''
there is also another solution by binary search but need to revise to further
'''
