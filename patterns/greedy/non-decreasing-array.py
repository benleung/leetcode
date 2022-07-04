class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        N = len(nums)
        is_modified = False
        
        lastlast = -inf
        last = nums[0]
        
        for i in range(1, N):
            if nums[i] < last:
                if is_modified:
                    return False
                else:
                    last = nums[i] if lastlast <= nums[i] else last
                    is_modified = True
            else:
                last = nums[i]
            lastlast = nums[i-1]
        
        return True
