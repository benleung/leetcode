'''
revisited on 2/26 (worth more revisit in future)
O(N)
almost one hour
'''
from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = 0
        d = {}  # first seen index
        
        for i,num in enumerate(nums):
            prefixSum += num
            prefixSum %= k
            if prefixSum == 0 and i>0:
                return True
            if prefixSum in d:
                if i - d[prefixSum] >= 2: # continuous subarray of size at least two
                    return True
            else:
                d[prefixSum] = i
        return False

'''
technique: 
combination of following ideas
- accumulative sum
- hashmap for sum of two
'''
from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(list) # We will store all indices with a given prefix sum % k in this.
        seen[0] = [-1]  # We have seen 0 before at index -1. Important to handle edge cases like this when nums = [23,2,4,6,6] and k = 7.
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            # If k = 0, any two consecutive 0's will return sum = 0 for us.
            if i > 0 and k == 0 and num == 0 and nums[i - 1] == 0:
                return True
            
            else:
                prefix_sum+=num # Keep track of prefix sum so far
                
                if prefix_sum % k in seen:
                    for index in seen[prefix_sum % k]: # Check if any of the indices with prefix sum mod k exists where (i - index >= 2). 
					# The reason for this is that if we have already found an element with this prefix sum % k value, then all elements 
					# after that index to current index (nums[index + 1:i + 1]) must sum up to something also divisible by k,
					# ie sum(nums[index + 1: i + 1]) % k == 0, this can be clearly seen from an example, so we return true in that case.
                        if i - index >= 2:
                            return True
                
                # Just add this index to our list of that prefix sum % k value.
                seen[prefix_sum % k].append(i)
                
        return False


'''
O(N^2) solution TLE


bad
careless on range(N-1)/N+1
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        dp = [0]*(N+1)
        cur = 0
        for i in range(N):
            cur += nums[i]
            dp[i+1] = cur
        for left in range(N-1):
            for right in range(left+2, N+1):
                target = dp[right] - dp[left]
                if target % k == 0:
                    return True
        return False
