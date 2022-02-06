# special case of middle element needs to be careful

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        h = {
            "6": "9",
            "8": "8",
            "1": "1",
            "9": "6",
            "0": "0"
        }

        for i in xrange(0, len(num)//2 ):
            if h.get(num[i]) != num[len(num)-1-i]:
                return False
        if len(num)%2 == 1:
            middle = num[len(num)//2]
            if middle == "8" or middle == "1" or middle == "0":
                return True
            else:
                return False
        
        return True
