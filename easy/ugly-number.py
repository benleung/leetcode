'''
4'for first solution, but didn't consider non-positive numbers

learnt
- should always look at range of data input to look for edge cases
'''

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n <= 0:
            return False
        
        while True:
            if n %2 == 0:
                n //= 2
                continue
            if n %3 == 0:
                n //= 3
                continue
            if n %5 == 0:
                n //= 5
                continue
            
            if n == 1:
                return True
            return False
            
        return True
