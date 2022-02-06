'''
17' (just slow in coding, can do faster)
miss out the case that there can be a->a->b
'''
class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        nextWordToMatch = None
        minCount = 3* (10**4) + 1
        curCount = 0
        for w in wordsDict:
            curCount += 1
            if nextWordToMatch == None and (w == word1 or w == word2):
                nextWordToMatch = word1 if w == word2 else word2
                curCount = 0
            if w == nextWordToMatch:
                minCount = min(minCount, curCount)
                nextWordToMatch = word1 if w == word2 else word2
                curCount = 0
            elif w == word1 or w == word2:
                curCount = 0
        return minCount
