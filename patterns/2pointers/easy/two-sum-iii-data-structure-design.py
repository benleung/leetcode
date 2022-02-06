# 23' for first time
# 5' for second with knowing the solution
'''
too many edge cases
e.g.
- add fast instead of find fast
- there can be multiple same number to be added, which isn't expressed in dict
- mistake that I should use if ... return True, instead of return ...
'''

class TwoSum(object):

    def __init__(self):
        self.h = {}

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        self.h[number] = self.h.get(number, 0)
        self.h[number] += 1

    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """

        for key, v in self.h.items():
            if self.h.get(value - key) != None:
                if value == key * 2:
                    if self.h.get(value - key) > 1:
                        return True
                else:
                    return True
        return False
