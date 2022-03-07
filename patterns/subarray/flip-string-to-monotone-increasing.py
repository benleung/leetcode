'''
5' after looking at hints, worth doing again
should realize the greedy is not possible, in that case, should try dp at each index
'''

from collections import Counter
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        N = len(s)
        ans = float("inf")
        
        dp = [0]
        for c in s:
            dp.append(dp[-1] + int(c))
        
        # number of 1 on left (exclusive) + number of 0 on right
        
        for i, count1left in enumerate(dp):
            count1right = dp[-1] - count1left
            countRight = N -i
            count0right = countRight - count1right
            
            ans = min(ans, count1left + count0right)
        
        return ans
