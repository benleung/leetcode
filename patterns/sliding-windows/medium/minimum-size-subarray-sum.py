'''
12'50

good
- able to think of the solution myself without hint

bad
- missing of the edge case of no matches
- forget to break (always necessary to iterate, in any possible conditions)
'''


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        l = 0
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            
            
            while cur >= target:
                ans = min(ans, i-l+1)
                
                # challenge one less element for the current right
                if l<i:
                    cur -= nums[l]
                    l += 1
                else:
                    break
        return ans if ans != float("inf") else 0
