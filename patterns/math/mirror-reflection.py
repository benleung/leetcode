'''
10'
about to deduce about lcm

'''
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        '''
        lcm_pq = x*q = y*p  where x, y are integer
        y: number of square
        '''
        lcm_pq = lcm(p, q)
        x = lcm_pq//q
        y = lcm_pq//p

        if y%2 == 0:
            return 0
        return 2 if x % 2 == 0 else 1
