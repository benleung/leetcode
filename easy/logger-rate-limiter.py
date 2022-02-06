'''
6'49" (perfect)

good
- one take pass
- good to take care of edge cases well

'''

class Logger(object):

    def __init__(self):
        self.lastPrintedSec = {} # string -> int

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.lastPrintedSec and timestamp - self.lastPrintedSec[message] < 10:
            return False
        else:
            self.lastPrintedSec[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
