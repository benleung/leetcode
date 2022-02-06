class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        hashtable = {}
        for num in nums:
            if hashtable.get(num) == None:
                hashtable[num] = 0
            else:
                hashtable[num] += 1
        for key, value in hashtable.items():
            if value >= n/2:
                return key

'''
5' (solution known in 30" but still takes too long to write the code)
- not familiar with dictionary
- should write the hashtable function much faster
- should use max on dictionary

retried a few times, fastest at 0'39" if solution already known

'''
