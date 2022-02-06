'''
about 15'

bad
- careless on reading question
- slow in writing logic for remaining letter all the same

'''


def isCapital(c):
    return ord(c) >= ord("A") and ord(c) <= ord("Z")

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        firstC = word[0]
        
        if not isCapital(firstC):
            for c in word[1:]:
                if isCapital(c):
                    return False
            else:
                return True
        else:
            # either all capital or all non-capital
            if len(word) == 1:
                return True
            
            # word[1] exists
            shouldRemainingCapital = isCapital(word[1])
            for c in word[1:]:
                if shouldRemainingCapital != isCapital(c):
                    return False
            return True
