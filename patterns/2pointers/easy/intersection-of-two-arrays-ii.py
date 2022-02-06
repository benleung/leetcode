'''
5' (perfect)

good
- able to think of the idea of count = min(h1.get(key,0), h2.get(key,0))
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h1 = {}
        h2 = {}
        for n in nums1:
            h1[n] = h1.get(n, 0)
            h1[n] += 1
        for n in nums2:
            h2[n] = h2.get(n, 0)
            h2[n] += 1
            
        sol = []
        for key in h1.keys():
            count = min(h1.get(key,0), h2.get(key,0))
            if count > 0:
                sol += [key]*count
        return sol
