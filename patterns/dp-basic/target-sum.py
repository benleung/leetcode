# 30' after some study
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        self.ans = 0
        dp = {} # (i, accSum) -> # of ways
        
        def backtrack(depth, accSum):
            
            if depth == N:
                if accSum == target:
                    return 1
                else:
                    return 0
            
            if (depth, accSum) in dp:
                return dp[(depth, accSum)]

            # try positive
            dp[(depth, accSum)] = backtrack(depth+1, accSum+nums[depth]) + backtrack(depth+1, accSum-nums[depth])
            return dp[(depth, accSum)]
        
        
        return backtrack(0,0)

# 4'
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        self.accSum = 0
        self.ans = 0
        
        def backtrack(depth=0):
            if depth == N:
                if self.accSum == target:
                    self.ans += 1
                return
            
            # try positive
            self.accSum += nums[depth]
            backtrack(depth+1)
            self.accSum -= nums[depth]
            
            # try negative
            self.accSum -= nums[depth]
            backtrack(depth+1)
            self.accSum += nums[depth]
        
        backtrack()
        return self.ans
            