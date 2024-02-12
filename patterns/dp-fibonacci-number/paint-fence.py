'''
39'
think in a backtracking with memorization manner
'''
class Solution:
    def numWays(self, n: int, k: int) -> int:
        ans = 0
        dp = {}   # (i, consecutive, color_count) -> answer

        def backtrack(i, consecutive):
            nonlocal ans

            if (i, consecutive) in dp:
                return dp[(i, consecutive)]

            if i == n:
                return 1   # this requires clear thought

            total = 0
            # same color
            if consecutive + 1 < 3:  # missed this
                total += backtrack(i+1, consecutive+1)

            # different color
            total += backtrack(i+1, 1)*(k-1)


            dp[(i, consecutive)] = total

            return total

        return backtrack(0, 0)

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
