# 48' (fail because too slow)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        nums.sort()
        self.dfs(3,0, [], nums)
        sol = []
        for i in range(len(self.result)):
            if self.result[i] not in sol:
                sol.append(self.result[i])
        return sol
    
    def dfs(self, depth, s, curList, rem):
        if depth == 0:
            return curList if s == 0 else []  # all combinations, should not return list?
        # not enough remember node
        if len(rem) == 0:
            return []

        for i,v in enumerate(rem):
            r = rem[i+1:]
            res = self.dfs(depth -1, s + v, curList+[v], r)
            if res != None and len(res) != 0:
                self.result.append(res)


# this problem has little bug such that the order is not well
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        nums.sort()
        self.dfs(3,0, [], nums)
        sol = []
        for i in range(len(self.result)):
            if i == 0 or self.result[i-1] != self.result[i] :
                sol.append(self.result[i])
        return sol
    
    def dfs(self, depth, s, curList, rem):
        if depth == 0:
            return curList if s == 0 else []  # all combinations, should not return list?
        # not enough remember node
        if len(rem) == 0:
            return []

        for i,v in enumerate(rem):
            r = rem[i+1:]
            res = self.dfs(depth -1, s + v, curList+[v], r)
            if res != None and len(res) != 0:
                self.result.append(res)

# think for long time but still fail
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:  # avoid duplicates
                    lo += 1

'''
22' after looking at hint

bad
<= instead of <


good
- able to write the following
while lo<hi and nums[lo] == nums[lo-1]:  # en
                    lo +=1 # skip duplicated index


learn
- use (,, ans) to allow the function to modify a variable
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        # empty list
        i = 0
        prevNum = None
        while i < len(nums) and nums[i]<=0:
            if prevNum != nums[i]:
                self.f(nums, i, ans)
            prevNum = nums[i]
            i += 1
        
        return ans
    
    def f(self, nums, i, ans):
        lo = i+1
        hi = len(nums)-1
        while lo<hi:
            if nums[i] + nums[lo] + nums[hi] == 0:
                ans.append([nums[i], nums[lo], nums[hi]])
                hi -= 1
                lo +=1
                while lo<hi and nums[lo] == nums[lo-1]:  # en
                    lo +=1 # skip duplicated index
            elif nums[i] + nums[lo] + nums[hi] < 0:
                lo += 1
            elif nums[i] + nums[lo] + nums[hi] > 0:
                hi -= 1
                
            