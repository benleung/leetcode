'''
6'40"

bad
- misunderstand the question in the first 3 min

good
- remember how to use collections.Counter(...)

learn 
- bit manipulation
- convert ascii number to string
'''
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        h = collections.Counter(s)
        for c in t:
            if h.get(c, 0) != 0:
                h[c] -= 1
            else:
                return c


# bitrise operation
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # Initialize ch with 0, because 0 ^ X = X
        # 0 when XORed with any bit would not change the bits value.
        ch = 0

        # XOR all the characters of both s and t.
        for char_ in s:
            ch ^= ord(char_)

        for char_ in t:
            ch ^= ord(char_)

        # What is left after XORing everything is the difference.
        return chr(ch)
