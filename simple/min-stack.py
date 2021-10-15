# 14 minutes

from collections import deque

class MinStack(object):

    def __init__(self):
        self.d = deque()
        self.minValStack = deque()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.d.append(val)
        if len(self.minValStack) == 0:
            self.minValStack.append(val)
        else:
            self.minValStack.append(min(self.getMin(), val))
        
        

    def pop(self):
        """
        :rtype: None
        """
        self.d.pop()
        self.minValStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.d[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minValStack[-1]
