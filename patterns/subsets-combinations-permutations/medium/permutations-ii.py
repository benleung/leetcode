'''
get used to append and pop

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
