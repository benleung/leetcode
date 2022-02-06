'''
# weekly-contest-278 3rd question
failed (time not calulated)

good
- recognize this is sliding window

learn
- meaning of pow() third parameter
- knowledge about mod (%) -> marked in anki
- reversed(..) is slow, use range(10, -1, -1) instead

analysis
hash(s, p, m) = (val(s[0]) * p0 + val(s[1]) * p1 + ... + val(s[k-1]) * pk-1) mod m.

'''

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(c):
            return ord(c)-96

        cur = 0
        ansLeftIndex = 0
        for i in range(k):
            cur = (cur + val(s[i-k])*(pow(power,i,modulo)))%modulo
        if cur == hashValue:
            ansLeftIndex = len(s)-k

        #sliding window
        for i in range(len(s)-k-1, -1, -1):  # reverse is better to avoid division problem
            cur = (cur - val(s[i+k])*(pow(power,(k-1),modulo)))%modulo # remove 
            cur *= power  #  a(power^0) + a(power^1) + a(power^2) + ... -> a(power^1) + a(power^2) + a(power^3) + ...
            cur = (cur + val(s[i]))%modulo
            if cur == hashValue:
                ansLeftIndex = i
        return  s[ansLeftIndex:ansLeftIndex+k]
