'''
about 20' (knowing the sol in advance)

good
- figure out the solution with my own effort only

learn
- find min length of a list of string
- for wordDict related problem , consider the length of word, so that you can write 

for l in range(minWordDictLength, maxWordDictLength+1):
                if dp[i+l] and s[i:i+l] in wordDict:
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        minWordDictLength = min(map(len, wordDict))
        maxWordDictLength = max(map(len, wordDict))
        wordDict = set(wordDict)
        S = len(s)
        
        dp = [False]*S + [True]*maxWordDictLength  # judge well on deciding initial value on additional base value
        for i in range(S-1, -1, -1):
            for l in range(minWordDictLength, maxWordDictLength+1):
                if dp[i+l] and s[i:i+l] in wordDict: # nice trick here
                    dp[i] = True
                    break
        
        return dp[0]
