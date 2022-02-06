'''
11' (slow)

- too slow for a standard binary search

learn
- binary search revise
- calucation of center between two point revised

'''

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        # edge case: 1
        
        left = 1
        right = num
        
        while left <= right: # <=?
            numberToTry = (left+right) // 2
            if numberToTry**2 == num:
                return True
            elif numberToTry**2 > num:
                right = numberToTry - 1
            elif numberToTry**2 < num:
                left = numberToTry + 1
        
        return False
