from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        h = Counter(words)
        '''
        when sort in decrasing, but the tie breaking requires increasing, use negative to organize them into both increase or both decreasing
        '''
        return heapq.nsmallest(k, h.keys(), key=lambda word: (-h.get(word), word))
