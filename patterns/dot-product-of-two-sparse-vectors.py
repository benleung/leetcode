# knowledge about sparse vectors
'''
naive approach
'''
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        nums1 = self.nums
        nums2 = vec.nums
        ans = 0
        for num1, num2 in zip(nums1, nums2):
            ans += num1*num2
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
