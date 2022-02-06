# 2' (too easy, nothing to study)

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        sol = 0
        while n != 0:
            sol += n % 2
            n /= 2
        return sol
