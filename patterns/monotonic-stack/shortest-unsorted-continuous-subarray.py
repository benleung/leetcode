class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minIndex = inf
        maxIndex = None
        curmax = None
        
        stack = [] # (index, val)  candidate for minIndex
        
        for i, num in enumerate(nums):
            # maxIndex
            if curmax != None and num < curmax:
                maxIndex = i 
            curmax = max(num, curmax) if curmax != None else num

            # minIndex
            while stack != [] and stack[-1][1] > num:
                index, _ = stack.pop()
                minIndex = min(index, minIndex)
            if i < minIndex:
                stack.append((i, num))
        
        return maxIndex - minIndex + 1 if minIndex != inf and maxIndex != None else 0
