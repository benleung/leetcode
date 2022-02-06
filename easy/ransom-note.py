

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        h = {}
        for c in magazine:
            h[c] = h.get(c,0)
            h[c] += 1
        
        for c in ransomNote:
            if h.get(c, 0) != 0:
                h[c] -= 1
            else:
                return False
        return True
