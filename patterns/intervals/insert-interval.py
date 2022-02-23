'''
1 hr

to learn:
- insert
- while-loop techique to insert a value to a sorted list
   - remove the list[i] that doesn't fit the requirement
   - insert can replace the slot
   - dun forget the size limit
- always prefer < instead of > (easy to visualize)
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = len(intervals) - 1
        while i>=0 and newInterval[0] < intervals[i][0]:
            i -= 1
        intervals.insert(i+1, newInterval)
        
        sol = []
        for i in range(len(intervals)):
            if sol == [] or sol[-1][1] < intervals[i][0]:
                sol.append(intervals[i])
            else:
                sol[-1][1] = max(intervals[i][1], sol[-1][1])
        return sol





'''
binary search method -> useless, because at the end 

to learn:
worst-case O(N) because the slice list operation has a time complexity of O(k) where k is the number of elements in the slice? So if the algorithm slices the whole list then it would be O(N) where N is the length of the 
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]):
        if not intervals:
            return [newInterval]
        
        def binarySearch1(arr, x):
            start = 0
            end = len(arr)-1
            while start<=end:
                mid = (start+end)//2
                if x[0] <= arr[mid][1]: end = mid-1
                else: start = mid+1
            return start

        def binarySearch2(arr, x):
            start = 0
            end = len(arr)-1
            while start<=end:
                mid = (start+end)//2
                if x[1] < arr[mid][0]: end = mid-1
                else: start = mid+1
            return start-1
        
        ind1 = binarySearch1(intervals, newInterval)
        ind2 = binarySearch2(intervals, newInterval)

        if ind1 > ind2:
            return intervals[:ind1] + [newInterval] + intervals[ind2+1:]
        
        else:
            x = min(intervals[ind1][0], newInterval[0])
            y = max(intervals[ind2][1], newInterval[1])
            return intervals[:ind1] + [[x,y]] + intervals[ind2+1:]
