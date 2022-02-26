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
