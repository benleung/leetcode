from collections import defaultdict
'''
20 min

pass in one time

not the fastest algorithm (slicing is expensive)

learning:
- rolling hash
  - use a number to represent a letter
    - change the base (not necessary decimal)
    - the formula is h = c0*(4^9) + c1*(4^8) +... + c9*1  (for 10 letter)
    - formula for updating h1 = h0 - c0*(4^9) + c1    # where h0 is old hash, h1 is new hash, c0 is old digit to remove, c1 is new digit to add
  - last time use index number to represent a letter, but not effective if the sequence of the letters are also important

'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        N  = len(s)
        if N<10:
            return []
        seen = defaultdict(int) # how many times seen, int (rolling hash) -> int
        # hashkey: 'A' -> 0, 'C' -> 1, 'G' -> 2, 'T' -> 3

        ans = []
        cur = deque()
        
        def insertOrIgnore(x):
            hashkey = tuple(x)
            seen[hashkey] += 1
            if seen[hashkey] == 2:  #happenmore than once
                ans.append("".join(x))

        for c in s[:10]:
            cur.append(c)
        insertOrIgnore(cur)
        
        for i in range(10,N):
            cur.popleft()
            cur.append(s[i])
            insertOrIgnore(cur)
        
        return ans


'''
second time
'''
from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        N  = len(s)
        if N<10:
            return []
        seen = defaultdict(bool) # how many times seen, int (rolling hash) -> int
        # hashkey: 'A' -> 0, 'C' -> 1, 'G' -> 2, 'T' -> 3
        ans = set()
        self.cur = 0
        
        def mapChToInt(ch):
            h = {
                'A': 0,
                'C': 1,
                'G': 2,
                'T': 3
            }
            return h[ch]
        
        def isSeen(old, new):
            self.cur -= 10**9*mapChToInt(old)
            self.cur *= 10
            self.cur += mapChToInt(new)
            if seen[self.cur]:
                return True
            else:
                seen[self.cur] = True
                return False
        
        # initial window
        for c in s[:10]:
            self.cur *= 10
            self.cur += mapChToInt(c)
        seen[self.cur] = True
        
        # other than intial one
        for i in range(10,N):
            if isSeen(s[i-10], s[i]):
                ans.add(s[i-9:i+1])
        
        return list(ans)

'''
optimized way, with base of 4
'''

from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        N  = len(s)
        if N<10:
            return []
        seen = defaultdict(bool) # how many times seen, int (rolling hash) -> int
        # hashkey: 'A' -> 0, 'C' -> 1, 'G' -> 2, 'T' -> 3
        ans = set()
        self.cur = 0
        
        def mapChToInt(ch):
            h = {
                'A': 0,
                'C': 1,
                'G': 2,
                'T': 3
            }
            return h[ch]
        
        def isSeen(old, new):
            self.cur = 4*(self.cur - (4**9)*mapChToInt(old)) + mapChToInt(new)
            if self.cur in seen:
                return True
            else:
                seen[self.cur] = True
                return False
        
        # initial window
        for i,c in enumerate(s[:10]):
            self.cur += mapChToInt(c)*(4**(9-i))
        seen[self.cur] = True
        
        # other than intial one
        for i in range(10,N):
            if isSeen(s[i-10], s[i]):
                ans.add(s[i-9:i+1])
        
        return list(ans)
