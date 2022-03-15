'''
10'
'''
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        
        # sort the boxes ascending order of numberOfUnitsPerBoxi
        boxTypes.sort(key=lambda x: x[1])
        
        while truckSize >0 and boxTypes:
            numberOfBoxes, numberOfUnitsPerBox = boxTypes.pop()
            numberOfBoxesToLoad = min(numberOfBoxes, truckSize)
            truckSize -= numberOfBoxesToLoad
            ans += numberOfBoxesToLoad* numberOfUnitsPerBox
        
        return ans
