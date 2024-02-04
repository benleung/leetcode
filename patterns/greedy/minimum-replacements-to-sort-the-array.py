
'''
good knowledge in division, should practice
[4,10,3]
[4,num,cur]
   ↑
[4,   2,2,3,3 ,3]
[4,   2,2,3,3 , cur]
len([2,2,3,3]) = ceil(num/cur)
min([2,2,3,3]) = num//len([2,2,3,3])
min([2,2,3,3]) = ceil(num/len([2,2,3,3]))
'''

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)
        cur = nums[-1]
        for i in range(N-1, -1, -1):
            num = nums[i]
            count = ceil(num / cur)
            cur = num // count
            ans += count - 1
        
        return ans
