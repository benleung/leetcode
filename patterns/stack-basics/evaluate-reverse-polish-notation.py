'''
14'
careless on 
stack.pop() - stack.pop() -> second - first
python syntax first time to know
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "*":
                result = stack.pop() * stack.pop()
            elif token == "/":
                second, first = stack.pop(), stack.pop()
                negation = 1 if second*first > 0 else -1
                result = negation * (abs(first) // abs(second))
            elif token == "-":
                second, first = stack.pop(), stack.pop()
                result = first - second
            elif token == "+":
                result = stack.pop() + stack.pop()
            else:
                result = int(token)
            stack.append(result)
        
        return stack[0]
