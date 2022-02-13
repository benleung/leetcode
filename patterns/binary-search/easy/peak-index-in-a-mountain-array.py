class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        N = len(arr)
        left = 0
        right = N-1
        
        while left<=right:
            center = (left+right)//2
            if self.isPeak(center, arr):
                return center
            elif arr[center] < arr[center+1]:
                left=center+1
            else:
                right = center-1
            
    def isPeak(self, i, arr):
        return arr[i-1] < arr[i] > arr[i+1]
