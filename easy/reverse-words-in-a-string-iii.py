'''
5'
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        
        word = deque()
        for c in s:
            if c == " ":
                ans.append("".join(word))
                word = deque()
            else:
                word.appendleft(c)
        ans.append("".join(word)) # forget this (last case handling)
        
        return " ".join(ans)
