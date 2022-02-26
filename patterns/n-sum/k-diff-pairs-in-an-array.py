
'''
not sure which but did a similar question which 

technqiue
- pair: count = dic.get(num-k, 0)

bad
- careless on k==0
'''

from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = Counter(nums)
        sol = 0
        for num, v in dic.items():
            count = dic.get(num-k, 0)
            if k == 0 and count >=2:    # k is the trick to avoid duplicate key being used
                sol += 1
            if k != 0 and count >=1:
                sol += 1
            
        return sol
