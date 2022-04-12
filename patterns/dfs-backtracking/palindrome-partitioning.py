'''
20'
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        candidate = []
        
        def isPalindrome(string):
            N = len(string)
            for i in range(N//2):
                if string[i] != string[N-i-1]:
                    return False
            return True
        
        def backtrack(i):
            N = len(s)
            if i >= N:
                ans.append(candidate.copy())
                return
            cur = ""
            for j in range(i, N):
                cur += s[j]
                if isPalindrome(cur):
                    candidate.append(cur)
                    backtrack(j+1)
                    candidate.pop()
            
        
        backtrack(0)
        
        return ans

'''
23'
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        def is_palidrome(s):
            N = len(s)
            for left in range(N//2):  # right center
                if s[left] != s[N-left-1]:
                    return False
            return True
        
        def backtrack(candidate, prefix, i): 
            # candidate: ["a","a","b"]
            # prefix: "a"
            
            if i == len(s):
                if prefix == []:
                    ans.append(candidate.copy())
                return
            
            
            # reserve for next index
            prefix.append(s[i])
            backtrack(candidate, prefix, i+1)
            prefix.pop()
            
            # check whether palidrome, and partition now
            prefix.append(s[i])
            if is_palidrome(prefix):
                candidate.append("".join(prefix))
                backtrack(candidate, [], i+1)
                candidate.pop()
            prefix.pop()
        
        backtrack([], [], 0)
        return ans

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
