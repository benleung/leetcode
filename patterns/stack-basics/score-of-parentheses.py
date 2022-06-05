'''
15' revisit on 4/14
failed once, 10' after knowing hint
'''
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = [0]
        
        for ch in s:
            if ch == "(":
                stack.append(0) # always
            else: # )
                node = stack.pop() #always
                stack[-1] += node*2 if node!= 0 else 1 # tricky
        
        return stack[0]
