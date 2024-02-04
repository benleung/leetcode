'''
30' with bug, need practice
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(start, end): #end exclusive
            if end-start == 1:
                return
        
            r_mid = (end+start+1)//2
            merge_sort(start, r_mid)
            merge_sort(r_mid, end)
            
            l = start
            r = r_mid
            sortedArray = []
            
            
            while l < r_mid or r < end:
                left = nums[l] if l < r_mid else inf
                right = nums[r] if r < end else inf
                if left < right:
                    sortedArray.append(left)
                    l += 1
                else:
                    sortedArray.append(right)
                    r += 1
            
            nums[start:end] = sortedArray[:]  
        
        merge_sort(0,len(nums))
        return nums
        