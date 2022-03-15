'''
15'
has a smarter solution in greedy, didn't study that yet
'''
from collections import defaultdict
class Solution:
    def numSquares(self, n: int) -> int:
        dp = defaultdict(lambda : float("inf"))
        
        dp[0] = 0
        square_number_base_max = int(math.sqrt(n))
        square_numbers = [base**2 for base in range(1, square_number_base_max + 1)]
        for i in range(n+1):
            for square_number in square_numbers:
                if i < square_number:
                    break
                dp[i] = min(dp[i], dp[i-square_number] + 1)
        return dp[n]
        