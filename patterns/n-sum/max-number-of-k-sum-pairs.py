'''
2'
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        h = defaultdict(int) # num -> count
        ans = 0
        for num in nums:
            if h[k-num] > 0:
                h[k-num] -= 1
                ans += 1
            else:
                h[num] += 1
        return ans
