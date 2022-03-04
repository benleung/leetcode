'''
with whiteboarding
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        N = len(temperatures)
        ans = [0] * N
        decStack = [] # (value, index)
        
        for i in range(N-1, -1, -1):
            while decStack:
                value, index = decStack[-1]
                if temperatures[i] < value:
                    decStack.append((temperatures[i], i))
                    ans[i] = index - i
                    break
                else:
                    decStack.pop()
                    
            else:
                decStack.append((temperatures[i], i))
                ans[i] = 0 # no future day for which this is possible
                
        return ans
