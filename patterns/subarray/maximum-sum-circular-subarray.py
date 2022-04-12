'''
10'
cycle: change
'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        N = len(nums)
        
        def maxSubarraySum(nums):
            dp = [0]*N # end with xxx
            ans = -inf
            for i in range(N):
                num = nums[i]
                if i == 0:
                    dp[i] = num
                else:
                    dp[i] = max(num, num + dp[i-1])
                ans = max(ans, dp[i])
            return ans
        
        def minSubarraySum(start,end): # end index exclusive
            M = end-start
            if M<=0:
                return 0
            dp = [0]*M # end with xxx
            ans = inf
            for i in range(M):
                num = nums[i+start]
                if i == 0:
                    dp[i] = num
                else:
                    dp[i] = min(num, num + dp[i-1])
                ans = min(ans, dp[i])
            return ans
            
        
        minInnerSum = min(0, minSubarraySum(1,N-1)) # all integer positive is possible
        
        return max(maxSubarraySum(nums), sum(nums) - minInnerSum)

'''
more then 30'
stuck at cycle 
'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        N = len(nums)
        
        left = [0]*len(nums)  # left[i] max sum that end with i
        inf = float('inf')
        ans = -inf
        
        for i, num in enumerate(nums):
            if i==0:
                left[i] = num
            else:
                left[i] = max(num, left[i-1] + num)
            ans = max(ans, left[i])

        max_head_sum = [-inf]*len(nums) #inclusive
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            max_head_sum[i] = max(max_head_sum[i-1], prefix_sum)
        
        max_tail_sum = [-inf]*len(nums) #inclusive
        prefix_sum = 0
        for i in range(N-1, -1, -1):
            num = nums[i]
            prefix_sum += num
            if i == N-1:
                max_tail_sum[i] = prefix_sum
            else:
                max_tail_sum[i] = max(max_tail_sum[i+1], prefix_sum)

        for i in range(N-1):
            ans = max(ans, max_head_sum[i] + max_tail_sum[i+1])

        return ans
