'''
10'
good to solve it myself, with very good familarity with dfs (with memorization)
should be able to solve by dp 2d, try next time
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        
        dp = {}
        N = len(s3)
        
        def dfs(left, right, i):
            if i == N:
                return True
            
            if (left,right,i) in dp:
                return dp[(left,right,i)]
            
            ch = s3[i]
            if left < len(s1) and  ch == s1[left]:
                if dfs(left + 1, right, i + 1):
                    return True
            if right < len(s2) and  ch == s2[right]:
                if dfs(left, right+1, i + 1):
                    return True
            dp[(left, right, i)] = False
            return False
        
        if N != len(s1) + len(s2):
            return False
        
        return dfs(0, 0, 0)
            