'''
good
thought of sliding windows in early stage
not careful enough in the logic in remove
'''


from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h = Counter(s1)
        S1 = len(s1)
        S2 = len(s2)
        
        if S1 > S2:
            return False
        
        numOfMatches = 0
        
        # initial setup of window
        for j in range(S1):
            if h.get(s2[j], 0) > 0:
                numOfMatches +=1
            if s2[j] in h:
                h[s2[j]] -= 1
        if numOfMatches == S1:
            return True
        
        for i in range(S1, S2):
            if s2[i-S1] in h: #initial element
                if h[s2[i-S1]]>=0:
                    numOfMatches -=1
                h[s2[i-S1]] += 1
                
            if h.get(s2[i], 0) > 0: #new element
                numOfMatches +=1
            if s2[i] in h:
                h[s2[i]] -= 1
            
            if numOfMatches == S1:
                return True
            
        return False
        