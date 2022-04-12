'''
24'

'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        N = len(s)
        stack = []
        
        count = Counter(s) # count of character left possible to add
        installed = set()
        
        def add(c):
            stack.append(c)
            installed.add(c)
        
        def pop():
            installed.remove(stack.pop())
            
        def can_pop():
            return stack and count[stack[-1]] >= 1
            
        for c in s:
            if c not in installed:
                while can_pop() and c < stack[-1]:
                    pop()
                add(c)
            count[c] -= 1
        
        return "".join(stack)

'''
1 hr
with limitted hints, and get reminded of remove-k-digits
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        N = len(s)
        ans = []
        last_seen = {}
        included_in_ans = set()

        for i in range(N-1, -1,-1):
            ch = s[i]
            if ch not in last_seen:
                last_seen[ch] = i
        
        for i, ch in enumerate(s):
            # skip if already in ans to avoid character duplicates in ans
            if ch in included_in_ans:
                continue
            
            # append in a way that ans[-1] < ch
            while ans and ans[-1] > ch:
                cannot_pop = last_seen[ans[-1]] < i
                if cannot_pop:
                    break
                else:
                    included_in_ans.remove(ans.pop())
            # here if ans[-1] < ch / ans is empty / ans[-1] cannot be poped:
            ans.append(ch)
            included_in_ans.add(ch)
                
            
        return "".join(ans)
