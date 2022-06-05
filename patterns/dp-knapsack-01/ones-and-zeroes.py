'''
60'

good question, should revise again
i is not necessary
  max(dp[][], dp[...-yy][...-xxx]) -> dp[][] is the value for last index
trick: reverse index

'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # o  m
        # l  n
        N = len(strs)
        dp =  [[0] * (n+1) for _ in range(m+1)]
        
        def dp_func(o, l):
            if not 0 <= o:
                return 0
            if not 0 <= l:
                return 0
            
            return dp[o][l]
        
        for i in range(N):
            counter = Counter(strs[i])
            
            for o in range(m, counter['0']-1, -1):
                for l in range(n, counter['1']-1, -1):
                    dp[o][l] = max(
                        dp[o][l],
                        dp_func(o-counter['0'], l-counter['1']) + 1
                    )
        
        return dp[m][n]
