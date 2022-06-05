'''
1 hr
'''
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)
        
        left = [-1]*N # index of next smaller value on the left, if n
        right = [N]*N # index of next smaller (or equal) value on the right
        
        monostack = []  # strictly increasing [(index, val)] 
        for i in range(N-1, -1, -1):
            while monostack and monostack[-1][1] >= arr[i]:
                monostack.pop()
            if monostack:
                right[i] = monostack[-1][0]
            monostack.append((i, arr[i]))

        monostack = []  # increasing [(index, val)]  (same val can exist in same stack)
        for i in range(N):
            while monostack and monostack[-1][1] > arr[i]:
                monostack.pop()
            if monostack:
                left[i] = monostack[-1][0] 
            monostack.append((i, arr[i]))
        
        
        
        
        ans = 0
        for i in range(N):
            left_count = i - left[i]
            right_count = right[i] - i
            
            ans += (arr[i] * left_count * right_count) % (10**9 + 7)
        
        return ans % (10**9 + 7)
