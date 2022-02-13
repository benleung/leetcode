'''
all permutations: within 5 mins
'''

from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pers = permutations(s1, len(s1))
        if len(s1)>len(s2):
            return False
        
        for per in pers:
            for i in range(len(s2)-len(per)+1):
                if s2[i:i+len(per)] == "".join(per):
                    return True
        return False
