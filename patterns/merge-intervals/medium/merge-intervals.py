'''
10'

good
- calc left and right well
- good decision on considering non overlapping as special case

learn
- revise on sort(key= ...)
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sol = []
        # sort here
        intervals.sort(key=lambda a: a[0])
        
        candidate = intervals[0]
        for i in intervals:
            if candidate[1] < i[0]:
                # doesn't overlap
                sol.append(candidate)
                candidate = i
            else:
                candidate = [ min(candidate[0],i[0]), max(candidate[1],i[1]) ]
        sol.append(candidate)
        
        return sol
