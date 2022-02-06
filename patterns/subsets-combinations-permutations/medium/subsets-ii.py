'''
Couter is necessary for cases of same value of different index item
'''


from collections import Counter
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        h = Counter(nums)
        sol = [[]]
        
        for k, v in h.items():
            for i in range(len(sol)):
                s = sol[i]
                for count in range(1,v+1):  # 0 is ignore
                    sol.append(s + [k]*count)
                
        return sol
