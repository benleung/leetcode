'''
24'
need prace on decoding string, similar to simplify-path
'''
class Solution:
    def calculate(self, s: str) -> int:
        numStack = []
        operatorStack = deque()
        
        curInt = 0
        for c in s:
            if c.isnumeric():
                curInt = curInt*10 + int(c)
            elif c == "+" or c == "-" or c == "/" or c == "*":
                if len(operatorStack)>0 and (operatorStack[-1] == "/" or operatorStack[-1] == "*"):
                    if operatorStack[-1] == "/":
                        numStack[-1] //= curInt
                    else: # *
                        numStack[-1] *= curInt
                    operatorStack[-1] = c
                else: # + / -
                    numStack.append(curInt)
                    operatorStack.append(c)
                curInt = 0
        else:
            numStack.append(curInt)
        
        if len(operatorStack)>0 and (operatorStack[-1] == "/" or operatorStack[-1] == "*"): 
            last_num = numStack.pop()
            if operatorStack[-1] == "/":
                numStack[-1] //= last_num
            else: # *
                numStack[-1] *= last_num
        

        
        operatorStack.appendleft('+')
        
        ans = 0
        for sign, num in zip(operatorStack, numStack):
            ans += num if sign == '+' else -num
        return ans
