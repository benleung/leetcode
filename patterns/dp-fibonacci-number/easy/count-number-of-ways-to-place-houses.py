'''
near robber house problem
'''
class Solution:
    def countHousePlacements(self, n: int) -> int:
        modulo = 10**9+7
        
        d = [0]*n
        d[0] = 2
        
        for i in range(1,n):
            d[i] = d[i-1] + (d[i-2] if i-2 >=0 else 1)
        
        return (d[n-1]**2) % modulo
