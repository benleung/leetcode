'''
3'

learnt
- intersect of set, union of set
- for ... in ... if ...
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h = {}
        for num in nums1:
            h[num] = True
        sol = set()
        for num in nums2:
            if num in h:
                sol.add(num)
        
        return list(sol)

# 2nd approach (2 sets intersection)
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        
        return [x for x in set1 if x in set2]
