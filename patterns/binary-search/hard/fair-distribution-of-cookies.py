'''
simialr to find-minimum-time-to-finish-all-jobs
bit mask technqiue is required
'''
from math import ceil
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        N = len(cookies)

        left = max(sum(cookies)//k, max(cookies))
        right = max(cookies)*ceil(N/k)
        
        print(left)
        print(right)
        
        dp = {}
        
        # dfs, try all combinations using the technqiue of bitmask
        def dfs(cookies, max_size, max_count):
            if max_count == 1:
                return sum(cookies) <= max_size
            
            C = len(cookies)
            for mask in range(1, 2**C):  # bitmask technqiues
                rest = []
                total = 0
                for i in range(C):
                    if (1 << i) & mask != 0:
                        total += cookies[i]
                    else:
                        rest.append(cookies[i])
            
                if total <= max_size:
                    if dfs(rest, max_size, max_count-1):
                        return True
            return False
            
        
        def is_feasible(candidate):
            if candidate in dp:
                return dp[candidate]
            
            dp[candidate] = dfs(cookies, candidate, k)
            return dp[candidate]

        while True:
            candidate = (left+right)//2
            if is_feasible(candidate) and not is_feasible(candidate-1):
                return candidate
            elif is_feasible(candidate):
                right = candidate - 1
            else:
                left = candidate + 1
        