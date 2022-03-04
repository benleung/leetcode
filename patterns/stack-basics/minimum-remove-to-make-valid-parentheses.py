'''
3'
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        skip = set()
        left = []
        
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c==')':
                if left:
                    left.pop()
                else:
                    skip.add(i)
            else:
                pass
        for i in left:
            skip.add(i)
        
        return "".join([c for i, c in enumerate(s) if i not in skip])
