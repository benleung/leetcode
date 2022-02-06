class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needleLen = len(needle)
        
        if needle == '':
            return 0
        
        for index, ch in enumerate(haystack):
            if haystack[index:index+needleLen] == needle and index + needleLen <= len(haystack):
                return index
        return -1