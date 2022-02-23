'''
how to think: select each element one by one (swap from either elemnet)
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        def backtrack(first):
            if first == N-1:
                ans.append(nums.copy())
            
            for i in range(first, N):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
                
        backtrack(0)
        return ans
