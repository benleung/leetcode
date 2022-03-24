'''
7'
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.left = 0
        self.right = 0
        
        sol = []
        
        
        def backtrack(candidates):
            # terminal condition
            if len(candidates) == 2*n:
                sol.append("".join(candidates))
                return

            is_left_possible = self.left < n
            is_right_possible = self.right < n and self.left > self.right
            
            if is_left_possible:
                candidates.append("(")
                self.left += 1
                backtrack(candidates)
                candidates.pop()
                self.left -= 1
            if is_right_possible:
                candidates.append(")")
                self.right += 1
                backtrack(candidates)
                candidates.pop()
                self.right -= 1
                
        
        
        backtrack([])
        
            
        return sol

'''

'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.leftCounter = 0
        self.rightCounter = 0
        sol = []
        
        def backtrack(candidates):
            if self.leftCounter + self.rightCounter == n*2:
                sol.append("".join(candidates))
                return
            
            if self.leftCounter == n:
                candidates.append(")")
                self.rightCounter += 1
                backtrack(candidates)
                candidates.pop()  # don miss this
                self.rightCounter -= 1
            elif self.leftCounter==self.rightCounter:
                candidates.append("(")
                self.leftCounter += 1
                backtrack(candidates)
                candidates.pop()
                self.leftCounter -= 1
                
            else:
                # each calling of backtrack will have new candidates, so for same depth can try different candidate ( not always need to use forloop)
                candidates.append("(")
                self.leftCounter += 1
                backtrack(candidates)
                candidates.pop()
                self.leftCounter -= 1
                
                candidates.append(")")  # for loop is not always necessary
                self.rightCounter += 1
                backtrack(candidates)
                candidates.pop()
                self.rightCounter -= 1
                
                
        
        backtrack([])
        return sol
