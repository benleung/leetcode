class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        returnValue = 0
        if x < 0:
            negative = -1
        else:
            negative = 1
        y = abs(x)
        
        
        
        
        while int(y) != int(0):
            reminder = y % 10
            returnValue = returnValue * 10 + reminder
            y = int(y/10)
        
        if returnValue >= pow(2, 31):
            return 0
        
        
        return returnValue * negative

# https://leetcode.com/problems/reverse-integer