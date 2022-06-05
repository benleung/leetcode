'''
12'
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = [] 
        candidate = []
        
        def dfs(number, remain_k, remain_n):
            if remain_k == 0:
                if remain_n == 0:
                    ans.append(candidate.copy())
                return

            if number == 10 or remain_n < 0:
                # terminal condition: no possible combination in this route (remain_n < 0)
                # or already reach the end
                return
            
               
            # include number in the combination
            candidate.append(number)
            dfs(number+1, remain_k-1, remain_n-number)
            candidate.pop()
            
            dfs(number+1, remain_k, remain_n)
        
        dfs(1, k, n)
        
        return ans
