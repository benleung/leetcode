
'''
revisit on 2/25
12'
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        d = [0]*N
        def dp(i):
            if i<0:
                return 0
            else:
                return d[i]
        
        for i in range(N):
            d[i] = max(dp(i-2) + nums[i], dp(i-1))
        return d[N-1]


'''
Method1: Recursive Approach with memorization

At each step, the robber has two options. If he chooses to rob the current house, he will have to skip the next house on the list by moving two steps forward.

robFrom(i)=max(robFrom(i+1),robFrom(i+2)+nums(i))

smaller set of houses that the robber has to consider. We will be working with the assumption that in the function call robFrom(i), the robber has to maximize their profit from i..N houses

robFrom(0) is the required solution

'''


'''
Method 2: DP

dynamic programming approach is simply a tabular formulation of the ideas presented above

robFrom[i]=max(robFrom[i+1],robFrom[i+2]+nums[i])

'''

'''
personal opinion:

hint: convert a problem of 0...n
to a subproblem of i..n
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0]*(N+1)
        dp[N-1] , dp[N] = nums[N-1], 0
        for i in range(N-2,-1,-1):
            dp[i] = max(dp[i+1], nums[i]+dp[i+2])
            
        return dp[0]

'''
Method 3: Optimized DP

we will be optimizing the space complexity here
To calculate the current value, we just need to rely on the next two consecutive values/recursive calls (no need the entire table)
'''
