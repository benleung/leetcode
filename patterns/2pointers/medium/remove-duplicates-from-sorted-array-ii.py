'''
8'30"

feel easy because did remove-duplicates-from-sorted-array before, which has similar idea


'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        
        if N == 0:
            return
        
        cur = nums[0]
        curCount = 0
        left = 0
        right = 0
        while right < N:
            if cur != nums[right]:
                curCount = 0
                cur = nums[right]
            if cur == nums[right]:
                curCount += 1            
            nums[left] = nums[right]

            if curCount < 3:
                left += 1
            right += 1
            
        del nums[left:]
        