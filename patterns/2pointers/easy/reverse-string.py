'''
2'
- perfect as I already master the center index
- 
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        middle = len(s)//2
        for i in xrange(0,middle):
            tmp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = tmp

'''

2' perfect

'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        for i in range(N//2):
            s[i], s[N-i-1]  = s[N-i-1], s[i]
