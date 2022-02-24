'''
revised on 2/24
(skip because seldom asked)

'''

'''
cannot solve due not insufficient knowledge in bit manipulations

learn
- observe by drawing a table to list out all values, and line them up
  - will know that common prefix is needed
- technqiue to find common prefix by shifting
'''


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
