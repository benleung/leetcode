'''
cannot solve and save time, so checked solution
a reminder again that after sort, the next element cannot have an earlier start tiem
'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = [] # [ end, ... ]
        
        if not intervals:
            return 0
        intervals.sort(key= lambda x: x[0])
        
        # first room
        heapq.heappush(heap, intervals[0][1])
        
        for start, end in intervals[1:]:
            
            if heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
                
        return len(heap)
