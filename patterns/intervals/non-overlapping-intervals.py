'''
16'
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        cur_end = None

        intervals.sort(key=lambda x:(x[0]))
        for interval in intervals:
            start, end = interval
            if not(cur_end == None or cur_end <= start):
                count += 1
                if end < cur_end:
                    cur_end = end
            else:
                cur_end = end
        
        return count

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
