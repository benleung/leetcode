
'''
15'

bad
- forget to realize 2 maps are required
- forget the case the 2 string may be have the same length

good
- remember zip
- 
'''
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        h1  = {} # a -> dog
        h2  = {} # dog -> a
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        for p, word in zip(pattern, words):
            
            if p in h1 and h1[p] != word:
                return False
            if word in h2 and h2[word] != p:
                return False
            
            h1[p] = word
            h2[word] = p
        return True

'''
8'
good to remember the one-to-one mapping is required
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pToS = {}
        sToP = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        for i,word in enumerate(words):
            if not pattern[i] in pToS:
                pToS[pattern[i]] = word
            else:
                if pToS[pattern[i]] != word:
                    return False
            if not word in sToP:
                sToP[word] = pattern[i]
            else:
                if sToP[word] != pattern[i]:
                    return False
                
            
        return True
