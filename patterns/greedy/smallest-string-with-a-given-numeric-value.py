'''
there is an optimized space solution worth studying
'''
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = deque()
        
        while k != 0:
            val = min(
                k-n+1,
                26
            )
            k -= val
            n -= 1
            ans.appendleft(chr(val+ord('a')-1))
        
        return "".join(ans)
