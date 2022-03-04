'''
14'
'''
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unvisited = set(nums)
        
        self.ans = 0
        self.cur = 0
        
        def dfs(num):
            self.cur += 1
            
            if num-1 in unvisited:
                unvisited.remove(num-1)
                dfs(num-1)
            if num+1 in unvisited:
                unvisited.remove(num+1)
                dfs(num+1)
            
        
        for num in nums:
            if num in unvisited:
                unvisited.remove(num)
                dfs(num)
                self.ans = max(self.ans, self.cur)
                self.cur = 0
        
        return self.ans

'''
O(n), but memory O(N) is not good enought
'''
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hi = max(nums)
        lo = min(nums)
        
        h = defaultdict(bool)
        for num in nums:
            h[num] = True
        
        ans = 0
        
        cur = 0
        
        for i in range(lo,hi+1):
            if h[i]:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 0
            
        return ans
