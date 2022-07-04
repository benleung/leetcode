'''
> 1h
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = 0
        lo  = (nums[0], 1)
        hi  = (nums[0], 1)
        for i in range(1, len(nums)):
            num = nums[i]
            next_hi = (num, lo[1]+1) if num > lo[0] else hi
            next_lo = (num, hi[1]+1) if num < hi[0] else lo
            lo, hi = next_lo, next_hi
            
        
        return max(lo[1], hi[1])
