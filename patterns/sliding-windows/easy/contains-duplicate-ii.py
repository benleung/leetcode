# 11' (too slow for this simple q)

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i_i, i_v in enumerate(nums):
            min_secondIndex = i_i+1
            max_secondIndex = min(i_i+k, len(nums)-1)
            for index2 in xrange(min_secondIndex, max_secondIndex+1):  # careless here
                if i_v == nums[index2]:
                    return True
        return False

# 4'20" (think about what data to store in hash table)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        h = {} # {v: i}
        for i, v in enumerate(nums):
            if v in h:
                if abs(i-h[v]) <= k:
                    return True
                else:
                    h[v] = i
            else:
                h[v] = i
        return False
