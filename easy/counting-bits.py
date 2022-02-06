'''
4'30" for less optimal sol

learn
- revise ord
- bin(...) can print binary representation

further learning
- what is the time complexity
- find time complexity of O(n) method
'''
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        sol = [0]* (n+1)
        for i in xrange(1,n+1):
            sol[i] = self.c(i)
        return sol
    def c(self, n):
        count = 0
        while n != 0:
            if n%2 == 1:
                count += 1
            n /= 2
        return count
