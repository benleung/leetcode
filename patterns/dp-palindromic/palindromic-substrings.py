'''
18'
careless:
- forget initialization
- forget dp[(..,..)] = true
'''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = defaultdict(bool) # (l, r) -> True : is palindrome
        N = len(s)
        ans = len(s) # string of length 1
        
        # when dist = N-1
        
        for i in range(N):
            dp[(i,i)] = True
        
        
        for dist in range(1, N): # 1 ~ N-1
            for l in range(0, N - dist): # 0.. dist-1
                r = l + dist
                is_middle_palindrome = dp[(l+1,r-1)] if dist != 1 else True
                if s[l] == s[r] and is_middle_palindrome:
                    ans += 1
                    dp[(l,r)] = True 

        return ans
