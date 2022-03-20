'''
20'
queue is a good way to handle this kind of sliding winows problem
'''
from collections import defaultdict
class HitCounter:

    def __init__(self):
        self.count = 0
        self.count_map = defaultdict(int)
        self.count_deque = deque()

    def removeLessThan(self, val): #inclusive
        while self.count_deque and self.count_deque[0] <= val:
            timestamp_to_pop = self.count_deque.popleft()
            self.count -= self.count_map[timestamp_to_pop]
            del self.count_map[timestamp_to_pop]
        
    def hit(self, timestamp: int) -> None:
        self.removeLessThan(timestamp-300)
        if self.count_map[timestamp] == 0:
            self.count_deque.append(timestamp)
        self.count_map[timestamp] += 1
        self.count += 1

    def getHits(self, timestamp: int) -> int:
        self.removeLessThan(timestamp-300)
        return self.count
