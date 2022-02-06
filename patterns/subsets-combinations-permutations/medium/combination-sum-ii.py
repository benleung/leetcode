'''
55' 

practice again
- keys = list(counter.keys())
- the need of using counter
- thought of use of counter and backtrack
  - backtrack is try if ok or not
  - using toegether with counter, can try with an upper limit of times
'''

from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        counter = Counter(candidates)
        keys = list(counter.keys())
        def backtrack(comb, start):
            s = sum(comb)
            if s == target:
                sol.append(list(comb))
                return
            elif s>target:
                return
            else:
                for i in range(start, len(keys)):
                    c = keys[i]
                    if counter[c] == 0:
                        continue
                    comb.append(c)
                    counter[c] -= 1
                    backtrack(comb, i)
                    comb.pop()
                    counter[c] += 1
        backtrack([], 0)
        return sol
