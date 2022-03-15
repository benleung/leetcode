'''
20' 
'''

class Solution:

    def __init__(self, w: List[int]):
        self.x = [] # index -> int (accSum)
        for weight in w:
            if len(self.x) == 0:
                self.x.append(weight)
            else:
                self.x.append(self.x[-1] + weight)


    def pickIndex(self) -> int:
        target = random.randrange(self.x[-1])
        left = 0
        right = len(self.x) - 1
        while left <= right:
            center = (left+right)//2
            if target < self.x[center] and (center == 0 or self.x[center-1] <= target):
                return center
            elif target >= self.x[center]:
                left = center + 1
            else:
                right = center - 1
