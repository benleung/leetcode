'''
8' 

- careless mistake on understanding the questions
- 
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for n in nums:
            h[n] = True
        for x in range(0,len(nums)+1):
            if h.get(x) == None:
                return x
        return 0
