# just translate my thinking into program
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        wordCount = 0
        shouldResetWordCountIfNextWordExists = False
        
        for ch in s:
            if ch != ' ':
                if shouldResetWordCountIfNextWordExists:
                    shouldResetWordCountIfNextWordExists = False
                    wordCount = 1
                else:
                    wordCount += 1
            else:
                shouldResetWordCountIfNextWordExists = True 
        return wordCount