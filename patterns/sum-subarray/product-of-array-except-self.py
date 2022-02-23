
'''
15'
solution for no additional memory is difficult

bad
- choosing i/i-1/i+1 is a bit tricky
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left = [1]*N
        right = [1]*N
        
        for i in range(N-1):
            left[i+1] = left[i]*nums[i]
        for i in range(N-1,0,-1):
            right[i-1] = right[i]*nums[i]
        ans = []
        for i in range(N):
            ans.append(left[i]*right[i])
        return ans
