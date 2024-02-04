'''
4'44" -> 5'46" revisted on dec 11

after knowing th ehint
'''


'''
14'

good
- able to translate the question to a very typical binary search problem

learn
- write 2-d array fater

'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        self.matrix = matrix
        left = 0
        right = len(self.matrix) * len(self.matrix[0]) - 1
        
        while left<=right:
            center = (left+right) // 2
            if self.mapIndexToValue(center) == target:
                return True
            elif self.mapIndexToValue(center) < target:
                left = center+1
            elif self.mapIndexToValue(center) > target:
                right = center-1
        return False
        
    # rtype: (i,j)
    def mapIndexToValue(self, i):
        xLength = len(self.matrix)
        yLength = len(self.matrix[0])
        
        y_index = i // yLength
        x_index = i % yLength
        return self.matrix[y_index][x_index]
