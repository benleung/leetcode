'''

learn
- all cominbations of sum that can be generated from a list
  - for num in nums: for x in dp.copy():
- dp.copy() to avoid the problem of dp being changed while iterating
- partition means all the elements are used
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2 == 1:
            return False
        
        dp = set({0})
        
        for num in nums:
            for x in dp.copy():
                total = x + num
                dp.add(total)
        
        
        return sum(nums) // 2 in dp
