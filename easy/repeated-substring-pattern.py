# 20'
# not familiar with string length
# optimized brute force
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)

        def isRepeatedInS(candidate, candidate_length):
            for i in range(N // candidate_length):
                index = i*candidate_length   # careless: didn't use index in the following
                if s[index:index+candidate_length] != candidate:
                    return False
            return True

        for length in range(1, N):
            if N % length != 0:
                continue
            candidate = s[:length]
            if isRepeatedInS(candidate, length):
                return True

        return False
