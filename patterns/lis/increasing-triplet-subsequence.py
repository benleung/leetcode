'''
by imagining a graph (think about peak)

(greedy) lower the hurdle to accept new element for sequence, based on each elemnet

the idea can actually be considered as a special case of longest-increasing subsequence

'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        if N <3:
            return False
        cur = 1
        while nums[cur-1] >= nums[cur]:
            cur += 1
            if cur == N-1: # last element also not accept
                return False
        # nums[cur-1] < nums[cur] here
        lo = nums[cur]
        lo1 = nums[cur-1]
        cur += 1
        while cur < N:
            if lo < nums[cur]:
                return True
            elif nums[cur-1] < nums[cur]:
                lo1 = min(lo1,nums[cur-1])
                lo = nums[cur]
            elif lo1 < nums[cur]:
                lo = nums[cur]
            cur += 1
        
        return False
