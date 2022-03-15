'''
1 hr, tricky to find it out
'''
from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        counter = Counter(s)
        
        ans = ""
        
        out = [0] * 10
        
        '''
        Letter "z" is present only in "zero".
        Letter "w" is present only in "two".
        Letter "u" is present only in "four".
        Letter "x" is present only in "six".
        Letter "g" is present only in "eight".
        '''
        
        out[0] = counter['z']
        for c in "zero":
            counter[c] -= out[0]
        
        out[2] = counter['w']
        counter['w'] -= out[2]
        counter['t'] -= out[2]
        counter['o'] -= out[2]
        
        out[4] = counter['u']
        counter['f'] -= out[4]
        counter['o'] -= out[4]
        counter['u'] -= out[4]
        counter['r'] -= out[4]
        
        out[6] = counter['x']
        counter['x'] -= out[6]
        counter['s'] -= out[6]
        counter['i'] -= out[6]
        
        out[8] = counter['g']
        counter['g'] -= out[8]
        counter['e'] -= out[8]
        counter['i'] -= out[8]
        counter['h'] -= out[8]
        counter['t'] -= out[8]
        
        out[3] = counter['h']
        counter['h'] -= out[3]
        counter['t'] -= out[3]
        counter['r'] -= out[3]
        counter['e'] -= out[3]*2
        
        out[5] = counter['f']
        counter['f'] -= out[5]
        counter['i'] -= out[5]
        counter['v'] -= out[5]
        counter['e'] -= out[5]
        
        
        out[7] = counter['s']
        for c in 'seven':
            counter[c] -= out[7]
        
        out[1] = counter['o']
        for c in 'one':
            counter[c] -= out[1]
        
        out[9] = counter['i']
        

        for i in range(10):
            ans += out[i] * str(i)
        
        return ans
