'''
24'
'''
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        N = len(nums)
        neg = [0]*N  # length of subarray with pos product that ends at i
        pos = [0]*N  # length of subarray with pos product that ends at i
        
        count = 0
        
        neg[0] = 1 if nums[0] <0 else 0
        pos[0] = 1 if nums[0] >0 else 0

        count = max(count, pos[0])
        for i in range(1, N):
            if nums[i] > 0:
                neg[i] = neg[i-1] + 1 if neg[i-1] != 0 else 0
                pos[i] = pos[i-1] + 1
            elif nums[i] < 0:
                neg[i] = pos[i-1] + 1
                pos[i] = neg[i-1] + 1 if neg[i-1] != 0 else 0
            else:
                neg[i] = 0
                pos[i] = 0
            
            count = max(count, pos[i])
        
        
        return count
