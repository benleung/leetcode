# basics
- if predicting future is required
  - try transverse from right to left
  - sometimes first left to right, then right to left
- Monotonic Stack is a common technique for cases that the next max/min value is needed

# Next max/min value/index
- first build from left to right
- next build from right to left (need to see the future)
```python
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

```
