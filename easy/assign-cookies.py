# ２pointer
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        ate_cookie = 0

        for i in range(len(g)):
            # has cookie for this child
            while j < len(s) and g[i] > s[j]:
                j += 1
            
            # eat the cookie
            if j < len(s) and g[i] <= s[j]:
                j += 1
                ate_cookie += 1
 

            if j >= len(s):
                return ate_cookie
            
        return ate_cookie
