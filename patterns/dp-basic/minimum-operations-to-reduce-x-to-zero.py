class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        right = {0: 0} # val to count
        N = len(nums)
        prefixSum = 0
        for i in range(N-1, -1, -1):
            prefixSum += nums[i]
            if prefixSum > x:
                break
            right[prefixSum] = N - i
        
        ans = inf
        remain = x
        for i in range(N+1):
            if i>0:
                remain -= nums[i-1]
            if remain < 0:
                break
            if remain in right and right[remain]+i <= N:
                ans = min(ans, right[remain]+i)
            
        
        return ans if ans != inf else -1
