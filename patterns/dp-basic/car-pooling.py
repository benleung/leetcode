'''
22' including explaination
similar to range sum
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        
         1 2 3 4 5 6 7
         2 2 2 2 2
             3 3 3 3 3
             4 4 4 4 4
             
         2         -2 
             
        
        
        L (1000) * T (1000)
        
        T log(T)
        
        T + L
        
        
        '''
        dp = [0] * 1001
        for trip in trips:
            [num, src, to] = trip
            dp[src] += num
            dp[to] -= num
        
        
        for i in range(1000):
            if i > 0:
                dp[i] += dp[i-1]
            if dp[i] > capacity:
                # print(dp)
                return False
        
        
        return True
