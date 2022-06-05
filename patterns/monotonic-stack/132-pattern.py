'''
very good question, should do again
'''

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        N = len(nums)
        min_left = [inf] # exclude self
        min_right = [inf]*N # exclude self
        
        # min_left
        for i in range(1, N):
            min_left.append(min(min_left[i-1], nums[i-1]))
        
        # min_right
        for i in range(N-2, -1, -1):
            min_right[i] = min(min_right[i+1], nums[i+1])
        
        for i in range(1, N-1):
            if min_left[i] < nums[i] and min_right[i] < nums[i]:
                return True
        else:
            return False
