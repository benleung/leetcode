'''
20'

good
- able to think of approach 1 (however sort is not efficient)

learn
- tuple can be used as key of dict
- tuple cannot be assign value, but array(list) can
'''


from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        patterns = {}  # pattern -> index
        
        def hashCounter(h):  # h is dict[chr: count]
            r = []
            for c in [chr(ord('a') + i) for i in range(26)]:
                r.append("#")
                r.append(str(h[c]))
            return "".join(r)
        
        
        for s in strs:
            pattern = hashCounter(Counter(s))
            if pattern in patterns:
                ans[patterns[pattern]].append(s)
            else:
                ans.append([s])
                patterns[pattern] = len(ans)-1
        
        return ans


'''
approach 2: after knowing the approach
'''

from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        patterns = {}  # pattern -> index of ans to add
        
        for s in strs:
            p = [0]*26
            for c in s:
                p[ord(c)-ord('a')] += 1
            p = tuple(p)
            if p in patterns:
                ans[patterns[p]].append(s)
            else:   # actually should use collections.defaultdict(list) to simplify this
                ans.append([s])
                patterns[p] = len(ans)-1
        return ans
