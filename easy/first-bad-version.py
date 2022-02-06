# 25min (know solution well but careless mistakes in variables)

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.firstBadVersionRe(1, n)
        
    def firstBadVersionRe(self, minV, maxV):
        firstBad = int((minV+maxV)/2)
        print(firstBad)
        isFirstBad = isBadVersion(firstBad)
        if (firstBad == 1 or not isBadVersion(firstBad-1)) and isFirstBad:
            return firstBad
        else:
            if isFirstBad:  # careless mistake here
                maxV = firstBad - 1
            else:
                minV = firstBad + 1
            return self.firstBadVersionRe(minV, maxV)
        