'''
7'

bad
- not careful about the case that the array is not full

learn
- shocked that 11/2 --> 5 instead of 5.5

good
- revised on from functools import reduce
- revised on from operator import add

'''


from functools import reduce
from operator import add

class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.l = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        
        if len(self.l) == self.size:
            self.l.pop(0)
        self.l.append(val)
        s = reduce(add,self.l, 0.0)
        return s/len(self.l)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
