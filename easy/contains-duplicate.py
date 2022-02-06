# 1'48"

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h = {}
        for n in nums:
            if h.get(n):
                return True
            h[n] = True
        return False
