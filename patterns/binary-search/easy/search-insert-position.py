class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        minimum = 0
        maximum = len(nums) - 1

        while True:
            if target > nums[maximum]:
                return maximum+1
            if target < nums[minimum]:
                return minimum
            
            middle  = int((maximum+minimum)/2)
            if nums[middle] == target:
                return middle
            if target > nums[middle]:
                minimum = middle+1
            else:
                maximum = middle-1

'''
second trial

calculation of return center if target < nums[center] else center+1 is slow
return left is ok
    reason: at the final situation, 
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left =0
        right = len(nums)-1
        
        while left<= right:
            center = (left+right)//2
            if nums[center] == target:
                return center
            elif nums[center] < target:
                left = center + 1
            else:
                right = center - 1
        return center if target < nums[center] else center+1 # left is better (at final situation, nums[right] < target < nums[left]) -> possible to duduce, but memorizing is bettter . at the same time, center is not realiable to use 


'''
third trial, 2' to reach this solution


imagine this table at utlimate position
right left  - -
1     3     5 6     (target: 2


it is possible thtat left is -1, or right is N
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            center = (left+right)//2
            if nums[center]==target:
                return center
            elif nums[center]<target:
                left = center+ 1
            else:
                right = center -1
        
        return left
