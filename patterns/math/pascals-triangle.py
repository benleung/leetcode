# first trial
# 5' think
# 14' code

# second trial
# 8' code
# key: match numRows with number of outter loops, match i with number of inner loops

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        toReturn = [[1]]
        
        for i in xrange(2, numRows+1):
            aboveRow = toReturn[-1]
            newRow = [aboveRow[0]]
            for j in xrange(0, i-2):
                newRow.append(aboveRow[j] + aboveRow[j+1])
            newRow.append(aboveRow[-1])
            toReturn.append(newRow)
        return toReturn


'''
for [column,row] of a pascal triangle, the value if nCr (where r is column, n is row, zero indexed)



'''
