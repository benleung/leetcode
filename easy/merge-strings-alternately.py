'''
5'

careless on append the rest of word (not efficient)
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1 = 0
        pointer2 = 0
        word = []
        while pointer1 < len(word1) and pointer1 < len(word2):
            if pointer1 < len(word1):
                word.append(word1[pointer1])
                pointer1 += 1
            if pointer2 < len(word2):
                word.append(word2[pointer2])
                pointer2 += 1
        return "".join(word) + word1[pointer1:] + word2[pointer2:]
