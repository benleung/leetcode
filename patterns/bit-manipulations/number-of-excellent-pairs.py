'''
number of 1 bits in (a & b) + number of 1 bits in (a | b)
= number of 1 bits in a + number of 1 bits in b

2 pointers problem is also included
'''
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        arr = []
        ans = 0
        nums = list(set(nums))
        for num in nums:
            arr.append(bin(num).count("1"))
        arr.sort()
        
        N = len(arr)
        
        left = 0
        right = len(arr)-1
        
        while left < N and right >= 0:
            if arr[left] + arr[right] >= k:
                ans += N - left
                right -= 1
            else:
                left +=1
                while left < right and arr[left] == arr[left-1]:
                    left +=1
        
        return ans
