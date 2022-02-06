
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
