'''
bad
- careless mistake on while loop thing
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped = deque(popped)
        
        if len(pushed) != len(popped):
            return False
        
        stack = []
        for element in pushed:
            if popped[0] == element:
                popped.popleft()
                while popped and stack and popped[0]==stack[-1]:
                    popped.popleft()
                    stack.pop()
            else:
                stack.append(element)
        if stack:
            return False
        return True
