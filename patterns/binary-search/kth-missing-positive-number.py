'''
should do again
only in-between values, cannot have destination statement
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def miss_elements_left_count(i):
            return arr[i] - i - 1

        left = 0
        right = len(arr) - 1
        
        if k > miss_elements_left_count(right):
            return arr[right] + k - miss_elements_left_count(right)
        if k <= miss_elements_left_count(left):
            return k

        while left < right-1:
            mid = (left+right)//2
            if k <= miss_elements_left_count(mid):
                right = mid
            else:
                left = mid
        
        # left + 1 == right now
        return arr[left] + (k - miss_elements_left_count(left))
        