'''
mistakes on using if instead of while

'''
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)
        
        
        i = 0
        
        while i < N:
            while i < N and nums[i] != 0:
                i += 1
            
            window_size = 1

            # nums[i] == 0 here
            while i < N and nums[i] == 0:
                ans += window_size
                window_size += 1
                i += 1
            
            
            
            
        
        return ans
