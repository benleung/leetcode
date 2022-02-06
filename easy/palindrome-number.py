'''
3'
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        center = len(x) // 2
        for i in range(0, center):
            if x[i] != x[len(x)- i -1]:
                return False
        return True
