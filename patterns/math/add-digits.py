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

'''
second time
'''
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sol = 0
        while num>=10:
            while num>0:
                sol += num%10
                num //= 10
            num = sol
            sol = 0
        
        return num


'''
math solution:
Digital Root
10 = 1*9 + 1
100 = 99*1 + 1

so, digital sum is n%9 (9 is the magic number)
'''
