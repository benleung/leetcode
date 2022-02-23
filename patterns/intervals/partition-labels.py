'''
30'

good to think of the answer by myself

learn
- sort is not needed
- revise: list(map(...))

careless
- forget to divide the case of total overlap and partly overlap

'''

from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        h = defaultdict(list)       # h[c][0] ->  firstseen   # h[c][1] -> lastseen
        for i,c in enumerate(s):
            if len(h[c])<2:
                h[c].append(i)
            else:
                h[c][1] = i
        
        intervals = []
        for key,value in h.items():
            if len(value) == 1:
                intervals.append([value[0],value[0]])
            else: # 2
                intervals.append(value)
        
        # intervals.sort(key=lambda x: x[0])
        
        for i in intervals:
            if ans == []:
                ans.append(i)
            else:
                if ans[-1][1] > i[0]:
                    # overlap
                    ans[-1][1] = max(ans[-1][1],i[1])
                else:
                    ans.append(i)
        
        return list(map(lambda x: x[1]-x[0]+1, ans))
