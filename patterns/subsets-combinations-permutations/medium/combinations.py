'''
15'

able to write backtrack well
'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        cur = []
        
        # handle the edge case of k > n
        if k>n:
            return []
        
        def backtrack(cur):
            if len(cur) == k:
                ans.append(cur.copy())
            
            start = cur[-1]+1 if cur != [] else 1  # the only tricky part here
            for i in range(start,n+1):
                cur.append(i)
                backtrack(cur)
                cur.pop()

        backtrack(0, cur)
        
        return ans
