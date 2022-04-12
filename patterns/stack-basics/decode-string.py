'''
51'
'''
class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        char_stack = [] # None for element that has [
        
        self.i = 0
        
        def getCount():
            string = ""
            while s[self.i].isnumeric():
                string += s[self.i]
                self.i += 1
            return int(string) # s[self.i] not numeric here
        
        def getString():
            string = ""
            while self.i< len(s) and s[self.i].isalpha():
                string += s[self.i]
                self.i += 1
            return string # s[self.i] not numeric here
        
        def print_stack(i):
            if len(count_stack) == 0:
                return ""
            
            ans = ""
            for i in range(i, len(count_stack)):
                ans += char_stack[i] * count_stack[i]
            return ans

        def find_index_with_None():
            for i in range(len(char_stack)-1, -1, -1):
                if char_stack[i] == None:
                    return i
            return 0 # unreachable
        
        def update_stack():
            i = find_index_with_None()
            char_stack[i] = print_stack(i+1)
            del char_stack[i+1:]
            del count_stack[i+1:]
        
        while self.i < len(s):
            c = s[self.i]
            if c == "[":
                char_stack.append(None)
                self.i += 1
            elif c == "]":
                update_stack()
                self.i += 1
            elif c.isalpha():
                if len(char_stack) == len(count_stack):
                    count_stack.append(1)
                char_stack.append(getString())
            else: #numerical
                count_stack.append(getCount())
        ans = print_stack(0)
        return ans

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
