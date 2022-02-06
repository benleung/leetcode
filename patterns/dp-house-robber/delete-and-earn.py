'''
1 hr

comment
- similar to house robber on the concept of avoiding adjacent house
- only need to consider one direction if using dp[i] = max value to delete and earn from i...end
'''


from collections import Counter
from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        h = Counter(nums)
        dp = defaultdict(int)  # dp[i] = max value to delete and earn from i...end
        keys = sorted(list(h.keys()))
        
        
        lastKey = keys[-1]
        dp[lastKey] = h[lastKey]*lastKey
        
        # edge case of not enough nums?
        
        i = len(keys)-2
        while i >=0:
            key = keys[i]
            
            if key+1 not in keys:
                nextKey = keys[i+1]
                dp[key] = max(dp[nextKey], h[key]*key + dp[nextKey])
                i -= 1
            else:
                nextKey = keys[i+1]
                nextNextKey = keys[i+2] if i+2 <len(keys) else None
                dp[key] = max(dp[nextKey], h[key]*key + dp[nextNextKey])
                i -= 1
            
            
            
        return dp[keys[0]]
