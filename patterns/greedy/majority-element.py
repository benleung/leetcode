'''
2'30"
remember the sol before
'''

'''
2'
remember the solution before
'''
class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            else:
                if candidate == num:
                    count += 1
                else:
                    count -= 1
        
        return candidate


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        hashtable = {}
        for num in nums:
            if hashtable.get(num) == None:
                hashtable[num] = 0
            else:
                hashtable[num] += 1
        for key, value in hashtable.items():
            if value >= n/2:
                return key

'''
5' (solution known in 30" but still takes too long to write the code)
- not familiar with dictionary
- should write the hashtable function much faster
- should use max on dictionary

retried a few times, fastest at 0'39" if solution already known

'''



'''
linear time and in O(1) space

assume that the majority element always exists in the array -> very strong
without assumption above, element with little frequency would possible be returned

technique
- candidate technique
    1. major problem: imagine of a competition which one strong majority (more than half of all) vs all other challengers
    2. score for the compeition: count
    3. dun know who is the candidate, but assuming he would try to attack and become candidate by count--, as it becomes the candidate officiailly it would count++
'''
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
