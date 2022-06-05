'''
knowledge about qudratic function is needed
30'
2 pointer is also needed
many careless mistakes here
'''


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:        
        def f(x):
            return a*(x**2) + b*x + c

        ans = []
        if a == 0:
            for num in nums:
                ans.append(f(num))
            isIncreasing = b > 0
            return ans if isIncreasing else ans[::-1]
        
        
        # a != 0
        center = -b/(2*a)
        
        right = 0 # len(nums) all the elemnt in nums smaller then center
        while right < len(nums) and nums[right] < center:
            right += 1
        left = right - 1 # -1: all the elemnt in nums larger then center
        
        while left>=0 or right < len(nums):
            left_diff = abs(nums[left]-center) if left>=0 else None
            right_diff = abs(nums[right]-center) if right < len(nums) else None
            
            if left_diff != None and right_diff != None:
                if left_diff < right_diff:
                    ans.append(f(nums[left]))
                    left -= 1
                else:
                    ans.append(f(nums[right]))
                    right += 1
            else:
                if left_diff != None:
                    ans.append(f(nums[left]))
                    left -= 1
                else:
                    ans.append(f(nums[right]))
                    right += 1
                    
        isMinCurve = a > 0
        
        return ans if isMinCurve else ans[::-1]
