'''
12'
'''
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        
        
        def isOneAddDistance(short, long):
            short_i = 0
            long_i = 0
            
            while short_i < len(short) and long_i < len(long):
                if short[short_i] == long[long_i]:
                    short_i += 1
                long_i += 1
                if long_i - short_i >= 2:
                    return False
            
            return True
        
        def isOneReplaceDistance(a, b):
            diff = 0
            
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                if diff >= 2:
                    return False
            
            return diff == 1
        
        if len(s) == len(t):
            return isOneReplaceDistance(s, t)
        
        if len(s)+1 == len(t):
            return isOneAddDistance(s, t)
        
        if len(s) == len(t) + 1:
            return isOneAddDistance(t, s)
        
        return False
