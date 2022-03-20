# Logical Deduction
from collections import defaultdict
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        
        for i in range(n):
            if candidate == i:
                continue
            if not knows(i, candidate) or knows(candidate, i):
                return -1
        
        return candidate
