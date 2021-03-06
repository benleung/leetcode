# 7'30" not a good solution
# class Solution(object):
#     def canAttendMeetings(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: bool
#         """
#         h = {} # time: Bool
#         for interval in intervals:
#             for i in xrange(interval[0], interval[1]):
#                 if i in h:
#                     return False
#                 h[i] = True
#         return True

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals = self.quicksort(intervals)
        for i in xrange(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
        
    def quicksort(self, intervals):
        if intervals == []:
            return []
        center = intervals[0]
        left = []
        right = []
        for i in xrange(1, len(intervals)):
            v = intervals[i]
            if v[0] < center[0]:
                left.append(v)
            else:
                right.append(v)
        return self.quicksort(left) + [center] + self.quicksort(right)


'''
2'40"
'''
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        N  = len(intervals)
        if N<= 1:
            return True
        intervals.sort(key=lambda x: x[0])
        for i in range(1,N):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        else:
            return True
