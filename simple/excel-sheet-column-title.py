from collections import deque

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        stringArray = deque()
        while columnNumber != 0:
            reminder = (columnNumber -1) % 26 # need to set to range 0~25 before %26
            columnNumber = (columnNumber-reminder) / 26
            stringArray.appendleft(str(chr(reminder + 65)))
        
        return "".join(stringArray)
