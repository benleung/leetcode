'''
30' including whiteboarding
good: solve the problem myself


'''
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        h = { a: 5, b: 3, c: 1} -> map heap
        
        "ab ab ab ac a"
        
        n log n
        
        
        
        '''
        counter = Counter(s)
        heap = []  # (freq, letter)
        
        def heappush(freq, letter):
            if freq == 0:
                return
            heapq.heappush(heap, (-freq, letter))
        
        def heappop():
            freq, letter = heapq.heappop(heap)
            return (-freq, letter)
        
        for letter, freq in counter.items():
            heappush(freq, letter)
        
        ans = ""
        lastLetter = ""
        
        while heap: # len > 2?
            nextLetter = heappop()
            
            # this is the last letter
            if len(heap) == 0:
                if nextLetter[0] != 1 or lastLetter == nextLetter[1]:
                    return ""
                else:
                    ans += nextLetter[1]
                    return ans
            
            if lastLetter != nextLetter[1]:
                # next letter is used
                ans += nextLetter[1]
                lastLetter = nextLetter[1]

                heappush(nextLetter[0]-1, nextLetter[1])
            else:
                # next next letter is used to avoid duplicate
                nextnextLetter = heappop()
                ans += nextnextLetter[1]
                lastLetter = nextnextLetter[1]
                
                heappush(nextLetter[0], nextLetter[1])
                heappush(nextnextLetter[0]-1, nextnextLetter[1])
        
        return ans
        