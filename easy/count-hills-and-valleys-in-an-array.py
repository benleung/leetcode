'''
10'
'''
class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate_hill = False
        candidate_valley = False
        count = 0
        
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                if candidate_valley:
                    count += 1
            elif nums[i-1] > nums[i]:
                if candidate_hill:
                    count += 1
            else:
                continue
            
            candidate_hill = nums[i-1] < nums[i]
            candidate_valley = nums[i-1] > nums[i]
            
        return count
