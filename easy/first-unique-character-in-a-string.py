'''
use two hashmap to store different data (first & double)

learn:
- 
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = set()
        doubled = set()
        for c in s:
            if  c in doubled:
                continue
            if c in first:
                doubled.add(c)
                first.remove(c)
            else:
                first.add(c)
        for i, c in enumerate(s):
            if c in first:
                return i
        return -1
