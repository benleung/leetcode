'''
learn about custom function for sorting
technique of index_l, index_r = i%L, i%R

following is a better solution for comparing two items
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
'''

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(l,r):
            L, R = len(l), len(r)
            LRmin, LRmax = min(L,R), L+R
            for i in range(L+R):
                index_l, index_r = i%L, i%R
                
                if l[index_l] < r[index_r]:
                    return -1
                elif l[index_l] > r[index_r]:
                    return 1
                
            return -1
            
        
        nums = deque(sorted(map(str, nums), key=cmp_to_key(cmp), reverse=True))
        while len(nums)>1 and nums[0] == "0":
            nums.popleft()
        
        return "".join(nums)
