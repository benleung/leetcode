class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        '''
        [2,4,5,10]
        
        dp = {
            2: 1
            4: 1 + 1 (2,2)
        }
        
        look at 10
        dp[10] += dp[2]*dp[5]
        
        O(N^2)
        '''
        dp = {}
        arr = sorted(list(set(arr)))
        
        # ans = 0
        for val in arr:
            dp[val] = 1
            
        for i, target in enumerate(arr):
            if target == 10:
                pass
            for j in range(i):
                lo = arr[j]
                if target % lo == 0:
                    hi = target // lo
                    dp[target] += dp[lo] * dp[hi] if hi in dp else 0
        
        # for key in h
        return sum(dp.values()) % (10**9+7)
