'''
50'
20' know the sol.
know the solution after walking through a few examples
queue is because of remove-k-digits
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        increasingQ = deque()
        
        # should try to write this function in faster manner
        # return the the smallest number in increasingQ larger than num, and insert there
        def findSmallestNumberLargerThan(num):
            if num < increasingQ[0]:
                tmp = increasingQ[0]
                increasingQ[0] = num
                return tmp
            
            left = 1
            right = len(increasingQ) - 1
            while left <= right:
                center = (left+right)//2
                if increasingQ[center] > num and increasingQ[center-1] <= num:
                    tmp = increasingQ[center]
                    increasingQ[center] = num
                    return tmp
                elif increasingQ[center] <= num:
                    left = center + 1
                else:
                    right = center - 1
        
        while nums:
            num = nums.pop()
            if not increasingQ or increasingQ[-1] <= num:
                increasingQ.append(num)
            else:
                # num > increasingQ[-1], next find the smallest number in increasingQ larger than num
                nums.append(findSmallestNumberLargerThan(num))
                break
        while increasingQ:
            nums.append(increasingQ.popleft())
