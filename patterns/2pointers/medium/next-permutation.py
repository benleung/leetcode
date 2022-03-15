'''
20' 
careless on < or <= bug
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        increasingQ = deque()
        j = 0
        for i in range(N-1,-1,-1):
            if i == N-1:
                increasingQ.append(nums[i])
            else:
                if nums[i] <increasingQ[-1]:
                    # binary search for a value just larger than nums[i] in increasingQ
                    left = 0
                    right = len(increasingQ)-1
                    while left <= right:
                        center = (left+right)//2
                        if nums[i] < increasingQ[center] and (center == 0 or increasingQ[center-1] <= nums[i]):
                            nums[i], increasingQ[center] = increasingQ[center], nums[i]
                            break
                        elif nums[i] < increasingQ[center] and nums[i] < increasingQ[center-1]:
                            right = center - 1
                        else:
                            left = center + 1
                    j = i + 1
                    break
                else:
                    increasingQ.append(nums[i])
                    
        while increasingQ:
            nums[j] = increasingQ.popleft() # from small to large
            j += 1

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
