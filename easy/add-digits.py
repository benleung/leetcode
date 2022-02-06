'''
4'
- wasted some time on writing reduce

learn
- syntax of reduce is 
- revised that from operator import sum

'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num))>1:
            s = 0
            for n in str(num):
                s += int(n)
            num = s
        return num
