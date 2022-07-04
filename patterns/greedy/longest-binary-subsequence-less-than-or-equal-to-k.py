'''
15'
'''
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = 0
        N = len(s)
        cur = 0
        for i in range(N-1, -1, -1):
            if s[i]=='0':
                ans += 1
            else: # '1'
                if 2**ans + cur <= k:
                    cur += 2**ans
                    ans += 1
        return ans
