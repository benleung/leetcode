'''
15'
smart to realize this question relates to stack
'''
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [[ch, count], ...]
        
        for ch in s:
            if stack == []:
                stack.append([ch, 1])
            else:
                prevCh = stack[-1][0]
                if prevCh == ch:
                    stack[-1][1] += 1
                else:
                    stack.append([ch, 1])
                
                if stack[-1][1] == k:
                    stack.pop()
        ans = []
        for ch, count in stack:
            for _ in range(count):
                ans.append(ch)
        return "".join(ans)
