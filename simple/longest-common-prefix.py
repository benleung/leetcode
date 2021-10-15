class Solution(object):
    
    def longestCommonPrefix(self, strs):
        result = []
        minLength = len(min(strs,key=len))
        for i in range(0, minLength):
            allSame = True
            ch = strs[0][i]
            for str in strs:
                if ch != str[i]:
                    allSame = False
                    break
            if not allSame:
                return ''.join(result)
            result += ch
        return ''.join(result)
        