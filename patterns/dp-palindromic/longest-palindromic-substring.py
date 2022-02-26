
'''
second trial (10')
for dp, possible to bottom up by increasing length
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        h = {}  #(left,right) : True/False
        maxLength = 0
        ans = (0,0)

        for i in range(N): # i+1: length
            for j in range(N-i):  # j = index
                if i == 0:
                    h[(j,j)] = True
                else:
                    isInBetweenPalindromic = h[(j+1,i+j-1)] if i != 1 else True
                    isPalindromic = isInBetweenPalindromic and s[j] == s[j+i]
                    h[(j,i+j)] = isPalindromic
                    if isPalindromic and i+1>maxLength:
                        maxLength = i+1
                        ans = (j,i+j)

        (left,right) = ans
        return s[left:right+1]

'''
about 1 hour

techniques
- it is possible to work out the way to expand the dp, by running 2 for loop, by incrementing length of string, and incrementing starting index 

- possible to 
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = [[True]*N for _ in range(N)]
        
        ans = s[0]
        maxLen = 0
        
        for i in range(N-1):
            dp[i][i+1] = s[i] == s[i+1]
            if dp[i][i+1] and 2 > maxLen:
                maxLen = 2
                ans = s[i:i+2]
        for i in range(2,N):
            for j in range(0,N-i):
                dp[j][i+j] = dp[j+1][i+j-1] and s[j] == s[i+j]
                if dp[j][i+j] and i+1 > maxLen:
                    ans = s[j:j+i+1]
        
        return ans



'''
copied from discussion (expand from center is the best answer)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ''
        for i in range(len(s)):
            p1 = self.get_palindrome(s, i, i+1)
            p2 = self.get_palindrome(s, i, i)
            p = max([p, p1, p2], key=lambda x: len(x))
        return p
    
    def get_palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
