'''
revisit on 4/12: 6'
revisited on 2/25
cannot find one pass solution, should revisit in future
'''

'''
7' after knowing the hints

learn
- 2d dp is not necessary for counting all possible number of arithmetic subarrays
    - dp[i] to represent combinations that last end index is i
- dp is not used as direct answer (ans += dp[i])



'''

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 2:
            return 0
        ans = 0
        dp = [0]*N
        for i in range(2, N):
            dp[i] = dp[i-1] + 1 if (nums[i] - nums[i-1] == nums[i-1] - nums[i-2]) else 0
            ans += dp[i]
        return ans


'''
TLE (N^2)

think by myself
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 2:
            return 0
        ans = 0
        dp = [[None]*N for _ in range(N)]
        for i in range(2, N+1):  # width of subarray
            for j in range(0, N - i + 1):
                diff = nums[j+i-2] - nums[j+i-1]
                if i == 2:
                    dp[j][j+i-1] = diff # for 2 elements, even dp not none doesn't mean it's arithmetic slice
                else:
                    if dp[j][j+i-2] == diff:
                        dp[j][j+i-1] = dp[j][j+i-2]
                        ans += 1
        return ans
