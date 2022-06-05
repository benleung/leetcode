'''
10'
'''
class Solution:
    def countVowelStrings(self, n: int) -> int:
        h = {} # (number, reamins) -> result
        
        def dfs(number, remains):
            key = (number, remains) 
            if key in h:
                return h[key]
            
            if remains == 1:
                h[key] = number
                return number
            
            ans = 0
            for i in range(1, number + 1):
                ans += dfs(i, remains-1)
            h[key] = ans
            return ans
            
        return dfs(5, n)
