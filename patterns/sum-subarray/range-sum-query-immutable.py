'''
3'
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0]*(len(nums)+1)
        cur = 0
        for i,num in enumerate(nums):
            cur += num
            self.dp[i+1] = cur

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right+1] - self.dp[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
