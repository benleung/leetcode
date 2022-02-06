'''
5'
https://leetcode.com/problems/subsets/solution/
'''

# approach 1 (i used)
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        for i in range(len(nums)+1):
            sol.extend(list(combinations(nums, i)))
        return map(lambda i: list(i), sol)   # common for using combinations

# approach 2 (cascading)
'''
At each step one takes new integer into consideration and generates new subsets from the existing ones
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output

# backtracking
'''
Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
