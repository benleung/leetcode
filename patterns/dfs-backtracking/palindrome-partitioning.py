'''
40'
got stuck in start index a bit
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        cur = [] # (start_index, end_index) e.g. length=1 means (0,1)
        
        def isPalidrome(lo, hi):
            hi -= 1
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True 
        
        def backtrack(start): # start_index
            if start == len(s):
                success_candidate = []
                # success
                for start_index, end_index in cur: 
                    success_candidate.append(s[start_index:end_index])
                ans.append(success_candidate)
            
            for i in range(start+1, len(s)+1):
                lo = start
                hi = i
                if not isPalidrome(lo, hi):
                    continue
                cur.append((lo, hi))
                backtrack(hi)
                cur.pop()
            
        backtrack(0)
        
        return ans
