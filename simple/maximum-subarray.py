
# too slow
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return max(nums[0], self.maxSubArrayLeft(nums[1:]), nums[0] + self.maxSubArrayLeft(nums[1:]))
        maximum = -10001
        for i in range(0, len(nums)):
            maximum = max(
                maximum,
                self.maxIncludeLeft(nums[i:])
            )
        return maximum
            
    def maxIncludeLeft(self, nums):
        maximum = -10001
        total = 0
        for i in range(0, len(nums)):
            total += nums[i]
            maximum = max(maximum, total)
        return maximum


### fast
def maxSubArray(self, nums: List[int]) -> int:
        min_seen_runsum = 0
        run_sum = 0
        ans = float('-inf')
        for num in nums:
            run_sum += num
            ans = max(ans, run_sum - min_seen_runsum) # a way to cancel beginning negative
            min_seen_runsum = min(min_seen_runsum, run_sum)
        return ans