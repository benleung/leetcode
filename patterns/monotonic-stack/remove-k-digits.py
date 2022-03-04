'''
revisited on 2/26, but cannot come up with optimal sol
should revisit in future
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        N = len(num)
        ans = deque()
        i = 0
        while i < N:
            if len(ans) ==0 or k == 0 or ans[-1] <= num[i]:
                ans.append(num[i])
                i += 1
            else:
                ans.pop()
                k -= 1
        
        for _ in range(k):
            ans.pop()
        
        while len(ans) > 1 and ans[0] == "0":
            ans.popleft()
        
        return "".join(ans) if len(ans)>0 else "0"

'''
good to think by myself, but have smarter solution

learn
- use of stack for the following situation
  - keep using the last element to compare, and after that use the second last elemnt
- special case of 0 (array of no elements)
- be careful of whether returning 0 or "0" (data type)
'''

from collections import defaultdict
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        N = len(num)
        left = 0
        right = 1
        indexToRemove = defaultdict(bool)
        ans = []
        
        while right < N and k>0: # take care of length of array 1
            while left >= 0 and num[left]>num[right] and k >0:
                if not indexToRemove[left]:
                    indexToRemove[left] = True
                    k -= 1
                left -= 1
                
            right += 1
            left = right - 1
            
            
        i = N-1
        while k > 0:
            if not indexToRemove[i]:
                k -= 1
                indexToRemove[i] = True
            i -= 1 # i cannot be negative because k <= num.length
        
        for i in range(N):
            if not indexToRemove[i] and not (ans == [] and num[i]=="0"):
                ans.append(num[i])
        
        return "".join(ans) if len(ans) >0 else "0"
