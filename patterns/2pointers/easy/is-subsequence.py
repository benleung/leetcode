'''
6'20"
good
- able to take care of edge care of length ==0
'''

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cur = 0
        if len(s) == 0:
            return True
        
        for c in t:
            if s[cur] == c:
                cur += 1
            if cur == len(s):
                return True
        else:
            return False
            