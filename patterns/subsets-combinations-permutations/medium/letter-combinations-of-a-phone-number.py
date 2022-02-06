'''
15' using product 

learn:
- revise better such that no need to refer to notion note

'''

from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        h = {}
        for i in range(2,7):
            firstLetter = ord('a')+(i-2)*3
            h[str(i)] = [chr(firstLetter), chr(firstLetter+1), chr(firstLetter+2)]
        h["7"] = ["p","q","r","s"]
        h["8"] = ["t","u","v"]
        h["9"] = ["w","x","y","z"]
            
        comb = [h[d] for d in digits]
        
        return list(map(lambda x: "".join(x), product(*comb)))


'''
10'

backtrack solution

good
- familiar with backtrack already
'''

from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        h = {}
        for i in range(2,7):
            firstLetter = ord('a')+(i-2)*3
            h[str(i)] = [chr(firstLetter), chr(firstLetter+1), chr(firstLetter+2)]
        h["7"] = ["p","q","r","s"]
        h["8"] = ["t","u","v"]
        h["9"] = ["w","x","y","z"]
            
        comb = [h[d] for d in digits]
        
        sol = []
        def backtrack(path):
            if len(path) == len(digits):
                sol.append("".join(path))
                return
            nexOptions = comb[len(path)]
            for nex in nexOptions:
                path.append(nex)
                backtrack(path)
                path.pop()
        backtrack([])
        return sol
            
