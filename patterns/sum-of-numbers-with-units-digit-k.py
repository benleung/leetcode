'''
edge case easily mistake, worth try again
'''
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        if k == 0:
            if num < 10:
                return -1
            else:
                return 1 if num%10 == 0 else -1

        ans = -1
        for candidate in range(num//k, 0, -1):
            if num - candidate*k >= 0 and (num - candidate*k) % 10 == 0 :
                ans = candidate
        
        return ans
