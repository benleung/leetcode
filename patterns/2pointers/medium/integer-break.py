
'''
d[1] has no meaning, but can help with building d[2] only, dun insist

pattern of building up number until target

bad
- trick that max(d[i-j],i-j) is necessary, since value itself is possibilty greater
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        d = [1]*(n+1) # d[1] = 1
        for i in range(2, n+1):
            d[i]= max([j * max(d[i-j],i-j) for j in range(1,i)])
        return d[n]
