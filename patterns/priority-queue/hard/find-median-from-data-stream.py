'''
good learning:
use of 2 heaps -> median
'''

class MedianFinder:

    def __init__(self):
        self.minHeap = [] # larger heap (even breaker)
        self.maxHeap = [] # smaller heap
        
    def pushMaxHeap(self, num):
        heapq.heappush(self.maxHeap, -num)
        
    def getMaxHeapTop(self):
        return -self.maxHeap[0]
    
    def popMaxHeap(self):
        return -heapq.heappop(self.maxHeap)

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0 or len(self.maxHeap) ==0:
            heapq.heappush(self.minHeap, num)
        else:
            if num > self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
            elif num < self.getMaxHeapTop():
                self.pushMaxHeap(num)
            else:
                heapq.heappush(self.minHeap, num)
        
        # rebalance number of elements in heaps
        if len(self.minHeap) - len(self.maxHeap) >= 2:
            self.pushMaxHeap(heapq.heappop(self.minHeap))
        if len(self.maxHeap) - len(self.minHeap) >= 2:
            heapq.heappush(self.minHeap, self.popMaxHeap())
        

    def findMedian(self) -> float:
        if len(self.minHeap) - len(self.maxHeap) == 1:
            return self.minHeap[0]
        elif len(self.maxHeap) - len(self.minHeap) == 1:
            return self.getMaxHeapTop()
        else: # both mush have heap
            return (self.getMaxHeapTop() + self.minHeap[0]) / 2
