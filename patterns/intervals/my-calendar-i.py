'''
good question
should study the balanced tree method https://leetcode.com/problems/my-calendar-i/solution/
'''


'''
solution 2: sortedlist
'''
from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.intervals = SortedList() # [(10,20), (20,30)]

    def book(self, start: int, end: int) -> bool:
        candidate = (start, end)
        
        i = self.intervals.bisect_left(candidate)
            
        last_interval = self.intervals[i-1] if i-1 >= 0 else None
        next_interval = self.intervals[i] if i < len(self.intervals) else None
        
        if last_interval != None and start < last_interval[1]:
            return False
        
        if next_interval != None and next_interval[0] < end:
            return False
        
        self.intervals.add(candidate)
        return True

'''
solution 1: brute force
'''
class MyCalendar:

    def __init__(self):
        self.intervals = [] # [[10,20], [20,30]]  sorted

    def book(self, start: int, end: int) -> bool:
        if not self.intervals:
            self.intervals.append([start, end])
            return True
        
        
        for i in range(len(self.intervals)):
            interval = self.intervals[i]
            if start <= interval[0]:
                if i-1 >=0 and start < self.intervals[i-1][1]:
                    
                    return False
                if interval[0] < end:
                    return False
                self.intervals.insert(i, [start,end])
                return True
        else:
            if start < self.intervals[-1][1]:
                return False
            else:
                self.intervals.append([start, end])
                return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
