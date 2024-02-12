'''
4'30"

good
- ddn't forget sorting

learn
- miss the case of interval overlap
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        intervals.sort(key=lambda x: (x[0], x[1]))

        for interval in intervals:
            start, end = interval
            if ans == []:
                ans.append(interval)
            else:
                if ans[-1][1] < start:
                    ans.append(interval)
                elif end <= ans[-1][1]:
                    pass
                else:
                    ans[-1][1] = end

        return ans
        

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
