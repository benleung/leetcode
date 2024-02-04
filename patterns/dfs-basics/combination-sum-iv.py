'''
should do again
complexity:
  O(target * N)
    depth of recursion is target a most
    N subproblem for each recursion
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        N = len(nums)
        
        dp = {}
        def dfs(remain):
            if remain == 0:
                return 1
            if remain in dp:
                return dp[remain]
            
            ans = 0
            for num in nums:
                if remain-num >= 0:
                    ans += dfs(remain-num)
            dp[remain] = ans
            return ans
        
        return dfs(target)
