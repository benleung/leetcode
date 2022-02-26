# 6' (simple)
# there is follow up question using byte

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        sol = 0
        for i in xrange(0,32):
            sol += n%2 * 2**(31-i)
            n = int(n/2)
        return sol
