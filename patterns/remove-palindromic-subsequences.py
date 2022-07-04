'''
understand subsequence (no need consecutive) is different from substring (need consecutive)
'''
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return 2
        else:
            return 1
