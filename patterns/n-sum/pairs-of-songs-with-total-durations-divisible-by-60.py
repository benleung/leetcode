'''
10' because did 2 sum before
'''

from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        '''
        brute force
        [30,20,150,100,40]
            __  __
        O(N^2)
        '''
        
        '''
        hash map
        
        60
        
        20 40 OK
        20 100 OK
        20 20 100 -> 2
        
        
        (a + b)%60 == 0 -> a%60 == (60-b)%60
        
        h[i%60] += 1
        
        ans += h[(60-j) %60 ]
        O(N)
        '''
        h = defaultdict(int)
        ans = 0
        for i in time:
            ans += h[(60-i) %60 ]
            h[i%60] += 1
        return ans
        