'''
similar to sum-of-subarray-minimums
with skills of 
explanation here: https://leetcode.com/problems/sum-of-subarray-ranges/discuss/1624222/JavaC%2B%2BPython-O(n)-solution-detailed-explanation
'''
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        
        # local min on left/right
        s = [(-inf, -1)] # monoIncreasingStack  (val,index)
        left = []
        right = [0]*N
        for i in range(N):
            while s[-1][0] > nums[i]:
                s.pop()
                #s[-1][0] is now smallerer than nums[i] (largest index that is smalle rthan nums[i])
            left.append(i - s[-1][1])
            s.append((nums[i], i))
        
        s = [(-inf, N)] # monoIncreasingStack  (val,index)
        for i in range(N-1, -1, -1):
            while s[-1][0] >= nums[i]:
                s.pop()
                #s[-1][0] is now smallerer than nums[i] (largest index that is smalle rthan nums[i])
            right[i] = (s[-1][1]-i)
            s.append((nums[i], i))
        
        for i in range(N):
            res -= left[i]*right[i]*nums[i]
        
        # local min on left/right
        s = [(inf, -1)] # monodecreasingStack  (val,index)
        left = []
        right = [0]*N
        for i in range(N):
            while s[-1][0] < nums[i]:
                s.pop()
                #s[-1][0] is now larger than nums[i] (largest index that is larger rthan nums[i])
            left.append(i - s[-1][1])
            s.append((nums[i], i))
        
        s = [(inf, N)] # monodecreasingStack  (val,index)
        for i in range(N-1, -1, -1):
            while s[-1][0]<= nums[i]:
                s.pop()
                #s[-1][0] is now larger than nums[i] (largest index that is larger rthan nums[i])
            right[i] = (s[-1][1] - i)
            s.append((nums[i], i))
        
        for i in range(N):
            res += left[i]*right[i]*nums[i]
        
        return res
