'''
30' slowly
repeatedly use the dp
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.ans = inf
        R = len(triangle)
        dp = [0] * R
        
        for row in range(R):
            C = len(triangle[row])
            for col in range(C-1, -1, -1):
                if col == 0:
                    dp[col] = dp[col] + triangle[row][col]
                elif col == C-1:
                    dp[col] = triangle[row][col] + dp[col-1]
                else:
                    dp[col] = min(
                        dp[col] + triangle[row][col],
                        triangle[row][col] + dp[col-1]
                    )
        
        return min(dp)
