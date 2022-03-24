'''
2' after a few practice
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        
        fast = 0
        slow = 0
        
        combo = 0
        candidate = None
        
        while fast < N:
            num = nums[fast]
            
            if candidate != num:
                combo = 1
                candidate = num
            else:
                combo += 1
                
            if combo < 3: # imagine appending to a new array
                nums[slow] = num
                slow += 1 # get ready for next
            fast += 1
        del nums[slow:]

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
        