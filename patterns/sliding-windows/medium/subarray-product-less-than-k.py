'''
finally gave up -> 8'47" after looking at hints

learning
- number of contiguous subarray combinations

not the followings are mutually exclusive
number of combinations with the 1st at the end
number of combinations with the 2nd at the end
number of combinations with the 3rd at the end
O|O|O
-|O|O
-|-|O

- when right end slides, there are no combinations that left should move to left
- feeling for sliding windows: right move first, and left follows
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        cur = 1
        
        # edge cases: [] ok,  [1] ok
        
        for r in range(len(nums)):
            cur *= nums[r]
            while cur >= k and l < r: # finish loop if l==r
                cur /= nums[l]
                l += 1
            if cur < k:
                ans += r-l+1
        
        return ans
