'''
sort -> greedy algorithm is often an effective approach

15'
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        
        intervals.sort(key=lambda x: x[1])
        cur = 1
        while cur<len(intervals):
            prevInterval = intervals[cur-1]
            curInterval = intervals[cur]
            if prevInterval[1] > curInterval[0]:
                count += 1
                del intervals[cur:cur+1]
            else:
                cur += 1
            
        
        return count
