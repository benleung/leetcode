'''
8'30"

complexity too slow

learn:
- this is a typical question of sliding window
- it is possible to compare Counter directly
- default value of Counter is 0 for each parameter, such that you can use s[x] += n directly

focus of sliding window
- remove start, and add end

'''

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        def isAnagram(s, p):
            h = Counter(p)
            for c in s:
                if h.get(c,0) != 0:
                    h[c] -= 1
                else:
                    return False
            return True
        
        ans = []
        for i in range(0, len(s)-len(p)+1):
            if isAnagram(s[i:i+len(p)], p):
                ans.append(i)
        return ans


'''
correct solution after looking at hints
'''
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        h_count = Counter(p)
        s_count = Counter()

        # case where length of s more than p
        
        ans = []
        for i in range(len(s)):
            s_count[s[i]] += 1
            if i >= len(p):
                s_count[s[i-len(p)]] -= 1
            if h_count == s_count:
                ans.append(i-len(p)+1)
        return ans
    
    