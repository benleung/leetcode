'''
8' including drawing graph
'''

from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sol = []
        candidate = []
        c = Counter(nums)
        keys = c.keys()

        def backtrack(depth):
            if depth == len(nums):
                sol.append(candidate.copy())
                return
            
            for key in keys:
                if c[key] > 0:
                    c[key] -= 1
                    candidate.append(key)
                    backtrack(depth+1)
                    c[key] += 1
                    candidate.pop()
                    
            
        backtrack(0)
        return sol

'''
get used to backtracking (append and pop)

'''
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                sol.append(list(comb))
                return     
            
            for num, count in counter.items():
                if count == 0:
                    continue
                counter[num] -= 1
                comb.append(num)
                backtrack(comb, counter)
                comb.pop()
                counter[num] += 1
                    
            
        backtrack([], Counter(nums))
        return sol
