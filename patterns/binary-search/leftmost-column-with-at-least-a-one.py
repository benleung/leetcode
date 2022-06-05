'''
24'
careless: while loop, forget to iterate += 1
clever to avoid over calling of api

a better solution: Start at Top Right, Move Only Left and Down
'''
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        curMin = inf
        rows, cols = binaryMatrix.dimensions()

        
        dp = {}
        
        
        def get(row, col):
            # reduce unnecessary call
            if (row,col) not in dp:
                dp[(row, col)] = binaryMatrix.get(row, col)
            return dp[(row, col)]
        
        # return inf if not found
        def binarySearch(row, lo, hi):
            while lo <= hi:
                center = (lo+hi)//2
                
                if get(row, center) == 1 and (center == 0 or get(row, center-1) == 0):
                    return center
                elif get(row, center) == 1 and get(row, center-1) == 1:
                    hi = center -1
                else:
                    lo = center +1
            
            return inf
        
        row = 0
        while curMin > 0 and row < rows:
            lo = 0
            hi = min(rows-1, inf)
            curMin = min(binarySearch(row, lo, hi), curMin)
            row += 1
            
        return curMin if curMin != inf else -1
