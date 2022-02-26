# 20 min 
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = 0
        right = len(numbers)-1
        
        while True:
            rightAnswerLessThanOrEqual = target - numbers[left]
            if numbers[right] == rightAnswerLessThanOrEqual:
                return [left+1, right+1]
            elif numbers[right] > rightAnswerLessThanOrEqual:
                right -= 1
            else:
                left += 1

# 2 min (remembered before)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        
        while left < right:
            total = numbers[left]+numbers[right]
            if total == target:
                return [left+1,right+1]
            elif total < target:
                left += 1
            else:
                right -= 1
