'''
extremely good question
cannot solve myself
'''

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        result = 0
        candidate = 0
        stack = [] # (val, min_steps_to_wait)
        N = len(nums)

        '''
        explaination

        [15,13,2,6,14]
        decreasing stack 
        *14* 14
        *6* 14 6
        *2* 14 6 2
        *13* 14 13 (remove 2, 6) 
        *14* 15 (2 steps is required to remove 13 instead of 1) <--- meaning for min_steps_to_wait


        '''

        for i in range(N-1, -1, -1):
            count = 0
            while stack != [] and stack[-1][0] < nums[i]:
                val, min_steps_to_wait = stack.pop()
                
                count = max(count + 1, min_steps_to_wait)
            result = max(result, count)
            stack.append((nums[i], count))
        
        return result
