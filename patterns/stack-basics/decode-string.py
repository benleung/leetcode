
'''
- Point: "" to represent [, wait for ] to happen and fill up

'''

'''
1 hr
not familiar with stack and decoding algorithm, need practice
'''
class Solution:
    def decodeString(self, s: str) -> str:
        numStack = deque()
        strStack = deque() # array of array of string
        
        self.i = 0
        
        def getInt():
            if s[self.i].isalpha():
                return 1
                # do not increment i
            
            curInt = 0
            while s[self.i].isnumeric():
                curInt *= 10
                curInt += int(s[self.i])
                self.i += 1
            return curInt
        
        while self.i < len(s):
            # hav to put to the top
            if s[self.i] == "]": # [] is invalid, so strStack must be more than len 1
                string = deque()
                while True:
                    isLast = strStack[-2] == ""
                    repeat = numStack.pop()
                    nextStr = strStack.pop()
                    
                    string.appendleft(nextStr * repeat)
                    
                    if isLast:
                        strStack[-1] = "".join(string)
                        break
                self.i += 1
                continue
            
            # fetch number
            numStack.append(getInt())
            
            # fetch character
            if s[self.i] == "[":
                strStack.append("")
                self.i += 1
            elif s[self.i].isalpha():
                strStack.append(s[self.i])
                self.i += 1
            else:
                # never come
                pass
                
        ans = ""
        while numStack and strStack:
            ans += strStack.popleft() * numStack.popleft()
        
        return ans
