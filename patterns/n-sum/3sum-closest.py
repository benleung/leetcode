'''
15'
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 0
        diff_with_target = float('inf')
        
        N = len(nums)
        nums.sort()
        
        i = 0  # unique i
        while i < N-2:
            i_num = nums[i] # 1st integer
            left = i + 1
            right = N - 1
            
            while left < right:
                new_sum = i_num + nums[left] + nums[right]
                new_diff = abs(target-new_sum)

                if diff_with_target > new_diff:
                    ans = new_sum
                    diff_with_target = new_diff
                    
                if new_sum < target:
                    left += 1
                else:
                    right -= 1
            
            while i < N-2 and i_num == nums[i]: 
                i += 1
            
        return ans
