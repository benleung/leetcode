'''
15'
good
- if remain < 0, i.e. we exceed the target value, we will cease the exploration here.

problem: 
- not able to handle ""
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol  = [
        ]

        def backtrack(comb, target):
            s = sum(comb)
            if s == target:
                sol.append(list(comb))
                return
            elif s > target:
                return
            else:
                for c in candidates:
                    if len(comb) == 0 or c >= comb[-1]:
                        comb.append(c)
                        backtrack(comb, target)
                        comb.pop()
        
        candidates.sort()
        backtrack([], target)
                
        return sol

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol  = [
        ]

        def backtrack(comb, start):
            s = sum(comb)
            if s == target:
                sol.append(list(comb))
                return
            elif s > target:
                return
            else:
                for i in range(start, len(candidates)):
                    c = candidates[i]
                    comb.append(c)
                    backtrack(comb, i)
                    comb.pop()
        
        candidates.sort()
        backtrack([], 0)
                
        return sol
