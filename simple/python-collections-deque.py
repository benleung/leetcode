from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        dict = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = deque()
        for ch in s:
            if ch in dict:
                if len(stack) != 0:
                    open = stack.pop()
                else:
                    return False
                if open != dict[ch]:
                    return False
            else:
                stack.append(ch)
            
            
        return len(stack) == 0