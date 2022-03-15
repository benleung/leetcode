'''
should use split instead of running ch by ch
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        # ..
        
        # /
        
        path_stack = []
        
        curWord = []
        
        for ch in path:
            if ch == "/":
                # ../
                if curWord == ['.','.']:
                    dot_count = 0
                    if path_stack:
                        path_stack.pop() # pop ..
                    if path_stack:
                        path_stack.pop() # pop the directory before
                # ./
                elif curWord == ['.']:
                    path_stack.pop() # pop .
                
                # skip ""//""
                if len(path_stack) >0 and path_stack[-1] == []:
                    continue 
                
                # new directory
                curWord = []
                path_stack.append(curWord)
            else:
                curWord.append(ch)
        
        # remove trailing /
        if len(path_stack) > 0 and path_stack[-1] == []:
            path_stack.pop()
        # remove trailing ..
        if len(path_stack) > 0 and path_stack[-1] == ['.','.']:
            path_stack.pop()
            if path_stack:
                path_stack.pop()
        # remove trailing .
        if len(path_stack) > 0 and path_stack[-1] == ['.']:
            path_stack.pop()
        
        return "/" + "/".join(map(lambda x: "".join(x), path_stack))
