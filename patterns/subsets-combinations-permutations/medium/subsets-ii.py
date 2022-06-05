'''
10' revisit on 4/14
backtrack
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sol = []
        counter = Counter(nums)
        keys = list(counter.keys())
        candidate = []
        def backtrack(i):
            if i == len(keys):
                sol.append(candidate.copy())
                return
            key = keys[i]
            for count in range(counter[key]+1):
                for _ in range(count):
                    candidate.append(key)
                backtrack(i+1)
                for _ in range(count):
                    candidate.pop()
                
        backtrack(0)
        
        return sol

'''
spend 20'
should revisit
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sol = [[]]
        nextSubsets =[]
        nums.sort()

        for i in range(len(nums)):
            isThisNumDuplicate = i>0 and nums[i-1] == nums[i]
            
            if not isThisNumDuplicate:
                nextSubsets = sol.copy()

            for j in range(len(nextSubsets)):
                nextSubsets[j] = nextSubsets[j] + [nums[i]]

            sol += nextSubsets
                
        return sol

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
