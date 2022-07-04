'''
7'
'''
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        window = set()
        left = 0
        cur = 0
        N = len(nums)
        
        for i in range(N):
            num = nums[i]
            while num in window:
                window.remove(nums[left])
                cur -= nums[left]
                left += 1
                
            window.add(num)
            cur += num
            ans = max(cur, ans)
        
        return ans
