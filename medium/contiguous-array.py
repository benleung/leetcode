'''
dun know answer

- need special trick (graph for +1, -1)
- index -1 is useful here
'''

from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        h = defaultdict(list)
        cur  = 0
        sol = 0
        h[0] = [-1]
        for i,v in enumerate(nums):
            cur += 1 if v == 1 else -1
            h[cur].append(i)
        for k, v in h.items():
            if len(v)>1:
                sol = max(sol , v[-1]-v[0])
            
        return sol
