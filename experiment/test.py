from collections import Counter, defaultdict, deque
from itertools import product

# a = str(sorted("tan"))

numbers = [1,3,2,9,4,5]
N = len(numbers)
maxQ = [[0, None] for _ in range(N)]
# [i, j] : i means the max num in the subarray of 0...i, j means the next max num index
# [[0, 1], [3, 3], [3, 3], [9, None], [9, None], [9, None]]

cur_max = numbers[0]
for i in range(1,N):
  cur_max = max(cur_max, numbers[i])
  maxQ[i][0] = cur_max

lastChangeIndex = None
for i in range(N-2,-1,-1):

  if maxQ[i][1] != maxQ[i+1][1]:
    lastChangeIndex = i
  maxQ[i][1] = lastChangeIndex
  
print(maxQ)
