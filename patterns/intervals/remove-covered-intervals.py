'''
8'50"

good
- able to use the sort technique (for multiple keys)
- able to realize sorting first can solve one end problem, enabling the possibility to use greedy algorithm
'''

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (-x[0], x[1]), reverse=True)
        
        cur = intervals[0][1]
        count = 1
        for i in intervals[1:]:
            if cur < i[1]:
                count += 1
                cur = i[1]
        
        return count
