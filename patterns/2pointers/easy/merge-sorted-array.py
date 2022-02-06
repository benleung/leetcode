class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        result = []
        i_m = 0
        i_n = 0
        while i_m < m or i_n < n:
            if i_n == n:
                result += [nums1[i_m]]
                i_m += 1
                continue
            if i_m == m:
                result += [nums2[i_n]]
                i_n += 1
                continue
            
            if nums1[i_m] > nums2[i_n]:
                result += [nums2[i_n]]
                i_n += 1
            else:
                result += [nums1[i_m]]
                i_m += 1
        
        for key, value in enumerate(result):
            nums1[key] = value