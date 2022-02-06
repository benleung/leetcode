
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        h = {}
        
        for c in s:
            h[c] = h.get(c, 0)
            h[c] += 1
        
        hh = {}
        for c in t:
            hh[c] = hh.get(c, 0)
            hh[c] += 1
        
        for key in h:
            if h.get(key) != hh.get(key):
                return False
        return True
