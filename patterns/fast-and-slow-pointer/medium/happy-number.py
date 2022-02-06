'''
8'

good
- trick of using set of visited to detect whether loops endlessly in a cycle

'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n not in visited:
            visited.add(n)
            if n == 1:
                return True
            n = self.sumOfSq(n)
        return False
    
    
    def sumOfSq(self, n):
        sum = 0
        while n != 0:
            sum += (n%10)**2
            n //= 10
        return sum
