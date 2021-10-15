#28 min
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        returnVal = 0
        for i in range(0, int(n/4) + 1):
            toAdd = ['a'] * 4
            addedCount = min(read4(toAdd), 4-max((i+1)*4-n, 0))
            
            
            
            buf[i*4:i*4+addedCount] = toAdd[0:addedCount]
            returnVal += addedCount
        return returnVal
