'''
good to learn that to deduce a key for hashmap, it's important to group the variable to one side of equation
j - i == nums[j] - nums[i]
=> nums[i] - i == j - nums[j]
'''
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # definition of good pair  
        # => j - i == nums[j] - nums[i]
        # => nums[i] - i == j - nums[j]
        # use "nums[i] - i" as the key for hashmap (items with same key are good pairs)
        diff = defaultdict(int)
        good_pair_count = 0
        N = len(nums)
        for i, num in enumerate(nums):
            good_pair_count += diff[num-i]
            diff[num-i] += 1
        
        return N*(N-1)//2 - good_pair_count
