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

'''
after understanding the solution (https://www.youtube.com/watch?v=RyBM56RIWrM)
observe how it repeats
dp not necessarily refer to dp[x-1], can be refered to a dp[x-offset] 
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)  # dp[0]  = 0
        
        if n == 0:
            return [0]
        
        dp[1] = 1
        offset = 1
        
        for i in range(2, n+1):
            if i == offset << 1:
                dp[i] = 1
                offset <<= 1
            else:
                dp[i] = 1 + dp[i-offset]
        
        
        return dp
