'''
- about 20' in total

a lot of knowlege about python was forgot
- split.(" ")
- sol = [None]*n
- xxx[0:len(word)-1] is possible (not include last element)

careless about
- sol[i-1] =   # forget -1
'''
class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        
        array = s.split(" ")
        sol = [None]*len(array)
        
        for word in array:
            i = int(word[-1])
            sol[i-1] = word[0:len(word)-1]
        
        return " ".join(sol)
