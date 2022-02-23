# 11' (speed for writing while loop can be improved)


# rowIndex1, no. of elements2, inner loop 0
# rowIndex2, no. of elements3, inner loop 1

# within 5' after knowing formula
from math import comb
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        if rowIndex==0:
            return [1]
        
        for i in range(rowIndex+1):
            ans.append(comb(rowIndex, rowIndex-i))
        return ans
