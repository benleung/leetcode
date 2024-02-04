'''
there is a binary search solution, wheter revise
→ did the binary search solution in kth-missing-positive-number instead
'''

'''
one pass (5')
'''
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        N = len(nums)
        for i in range(N-1):
            num = nums[i]
            nextNum = nums[i+1]
            inBetweenCount = nextNum-num-1
            if k <= inBetweenCount:
                return num + k
            else:
                k -= inBetweenCount
        else:
            return nums[-1] + k
