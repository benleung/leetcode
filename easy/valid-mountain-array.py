'''
7'

good
- finish in one pass handling all cases


'''

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        
        # increasing
        while i<len(arr)-1:
            # iterate and continue only if the next element is larger
            
            if arr[i]>=arr[i+1]:
                break
            i += 1
        if i == 0 or i == len(arr)-1:
            # has iterate and not reach the end of array yet
            # edge case of empty list can be handled here
            return False
        
        # decreasing
        while i<len(arr)-1:
            # iterate and continue only if the next element is smaller
            if arr[i]<=arr[i+1]:
                break
            i += 1
        if i != len(arr)-1:
            return False

        return True
