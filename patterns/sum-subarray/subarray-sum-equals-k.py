'''
brute force 8'

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N  = len(nums)
        count = 0
        for i in range(N):
            cur = 0
            for j in range(i, N):
                cur += nums[j]
                if cur == k:
                    count += 1
        
        return count


'''
approach 2: Cumulative Sum

technqiue
- d[i] is used to store the cumulative sum of numsnums array up to the element corresponding to the (i-1)^{th}(i−1) 
th index
- if the cumulative sum up to two indices, say ii and jj is at a difference of kk i.e. if sum[i] - sum[j] = ksum[i]−sum[j]=k, the sum of elements lying between indices ii and jj is kk.


bad: edge case thinking
- whether [] is a combination?
- be careful of 0 or negative number
  - dun break


'''


'''
approach 3: hashmap + accumulative sum

- idea
  - sum of two number -> hashmap
  - subarray sum -> accumulative sum
'''
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N  = len(nums)
        count = 0
        h = defaultdict(int)
        h[0] = 1
        
        cur = 0
        for num in nums:
            cur += num
            if cur-k in h:
                count += h[cur-k]
            h[cur] += 1
        return count
