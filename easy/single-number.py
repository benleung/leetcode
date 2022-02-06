class Solution(object):
    def singleNumber(self, nums):
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 0
            dict[num] = dict[num] + 1
        for key, value in dict.items():
            if value == 1:
                return key
        return 0

# https://leetcode.com/problems/single-number/discuss/1494917/XOR-solution-C-and-C%2B%2B