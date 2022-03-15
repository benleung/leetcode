'''
30'
think in backtracking way, but easier if think from dp
'''
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if k == 1:
            return 1 if n <= 2  else 0 
        self.ans = 0
        dp = {}
        
        def backtrack(depth, count = 1):
            if depth == n:
                return count

            if (depth, count) in dp:
                return dp[(depth, count)]
            
            count = count*(k-1) if depth != 0 else k

            result = 0
            if depth + 1 <= n:
                dp[(depth +1, count)] = backtrack(depth +1, count)
                result += dp[(depth +1, count)]
            if depth +2 <= n:
                dp[(depth +2, count)] = backtrack(depth +2, count)
                result += dp[(depth +2, count)]
            
            return result
        return backtrack(0)
