'''
17'
realize the answer when imagine the final scenarios at each index
'''
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        N  = len(data)
        M = 0
        for d in data:
            if d == 1:
                M += 1
        
        cur = 0 # number of zeros = number of swaps required
        for i in range(M):
            if data[i] == 0:
                cur += 1
        ans = cur
        
        for i in range(1, N-M+1):
            old = data[i-1]
            if old == 0:
                cur -= 1
            
            new = data[i+M-1]
            if new == 0:
                cur += 1
            
            ans = min(ans, cur)
        
        
        return ans
        