'''
5' 
programming skills only
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        
        def add(a,b):
            if a == b:
                ans.append(str(a))
            else:
                ans.append(str(a) + "->" + str(b))
        
        if len(nums) == 0:
            return []
        lo = nums[0]
        hi = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] == hi + 1:
                hi += 1
            else:
                add(lo,hi)
                lo = hi = nums[i]
        
        add(lo,hi)
        return ans
