'''
aroudn 10' (not carefully calculated)
complexity calculation is a bit tricky

'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        monoStack = [] # from large to small
        
        N = len(nums2)
        h = {}
        
        for i in range(N-1, -1, -1 ):
            num = nums2[i]
            while monoStack != [] and num >= monoStack[-1]:
                monoStack.pop()
            else:
                # monoStack is empty or h[num] < monoStack[-1]:
                if not monoStack:
                    h[num] = -1
                else:
                    h[num] = monoStack[-1]
                monoStack.append(num)
            
        sol = []
        for num in nums1:
            sol.append(h[num])
        return sol
