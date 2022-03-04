from collections import Counter, defaultdict, deque, OrderedDict
import heapq
from itertools import product

# a = str(sorted("tan"))

x = []
heapq.heappush(x, 200)
heapq.heappush(x, 10)
heapq.heappush(x, 9)
print(x[0])
print(heapq.heappop(x))
print(heapq.heappop(x))
