'''
3' understand q.

17'40" finish coding


bad
- edge case of hour <= 12 instead of <12 is wrong

good
- almost one take
- know the trick of 
hours = [8,4,2,1]
minutes = [32,16,8,4,2,1]
to represent each bit

- know that combinations(range(10),turnedOn) is not changed
- know the trick of 
if i<4:
    hour += hours[i]
if i>=4:
    minute += minutes[i-4]


learn
- 


'''
from itertools import combinations

class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        hours = [8,4,2,1]
        minutes = [32,16,8,4,2,1]
        sol = []
        for tup in combinations(range(10),turnedOn):
            hour = 0
            minute = 0
            for i in tup:
                if i<4:
                    hour += hours[i]
                if i>=4:
                    minute += minutes[i-4]
            if hour < 12 and minute <= 59:
                sol.append("{0}:{1}".format(hour, self.f(minute) ))
        return sol
    def f(self, number):
        return str(number) if number>= 10 else "0{0}".format(number)
