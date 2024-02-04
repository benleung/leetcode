'''
failed
actual this problem is similar to partition-equal-subset-sum, but no dp-01
the technique used here is bitmask

very good question
'''
class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        T4 = sum(nums)
        if T4%4 != 0:
            return False
        T = T4//4
        
        N = len(nums)
        
        dp = {}  # (mask, done) -> True/False
        
        def bitmask_bit_from_left(mask, i, N): #-> this is useful
            return mask & 1<<(N-1-i)
        
        # yield (num, i) that matches with 1 -> this is useful
        def bitmask_num(mask, nums):
            N = len(nums)
            for i in range(N):
                if mask&(1<<(N-1-i)):
                    yield (nums[i], i)
        
        # sum up num that matches with 0 -> this is useful
        def bitmask_total(mask, nums):
            # 1100 [a, b, c, d]
            # return : a + b
            total = 0
            for i in range(len(nums)):
                if mask&(1<<(len(nums) - 1 - i)) == 0:
                    total += nums[i]
            return total
        
        
        # mask: available matches
        def backtrack(mask, done):
            if (mask, done) in dp:
                return dp[(mask, done)]
            
            if done == 3:
                return True
            
            total = bitmask_total(mask, nums)
            remain = total%T
            ans = False
            for num, i in bitmask_num(mask, nums):
                if remain + num <= T:
                    ans = backtrack(mask^(1<<(N-1-i)), done + 1 if remain + num == T else done)  # ^ to reverse a 1 to 0
                    if ans:
                        break
            dp[(mask, done)] = ans
            return ans
        
        ans =  backtrack((1<<N) - 1, 0)
        return ans


'''
TLE
note that the leetcode solution about dfs is also TLE
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        T4 = sum(matchsticks)
        if T4%4 != 0:
            return False
        T = T4//4

        def backtrack(i, a, b, c):
            if i == len(matchsticks):
                return False
            
            if a+b+c == 0:
                return True
            
            matchstick = matchsticks[i]
            
            if a - matchstick >= 0 and backtrack(i+1, a-matchstick, b, c):
                return True
            if i != 0 and b - matchstick >= 0 and backtrack(i+1, a, b-matchstick, c):
                return True
            if i !=0 and c - matchstick >= 0 and backtrack(i+1, a, b, c-matchstick):
                return True
            if backtrack(i+1, a, b, c):
                return True
            return False
        
        return backtrack(0, T, T, T)
