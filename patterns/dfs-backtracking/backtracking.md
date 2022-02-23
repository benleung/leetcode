# definition
Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.

# how to think
example of binary-watch

0. draw the tree, write the skeleton of backtrack function

![picture 3](images/c1f761fe255130070e2db2da4169edbcd4dc7b5a035f943c7587bb6a3264b19f.png)  
``` python
ans = []  # ans the stores what target has been found

self.remains = n  # status that stores the current choices (given the number of "selected choices" are limited, this is a common technique if array is not used)

self.h = 0 # status that stores the current choices
self.m = 0 # status that stores the current choices
def backtrack(depth):  # depth
  ...

```


1. terminal condition
  - imagine the first depth finish (how much depth to reach)
```python 
if self.remain == 0:
    ans.append("{0}:{1:02d}".format(self.h,self.m))
    return
```

2. rule out the conditions that doesn't find requirement
- depth is over the limitation
- condition is obviously not matched


```python 
if start>=len(lights) or not (0<=self.h<12 and 0<=self.m<60):
    return
```

3. backtrack for one branch
```python
# this bit is turned on
self.h, self.m = self.h+dh, self.m+dm
self.remain -= 1
backtrack(depth + 1)  # note that depth is proceeded here
self.remain += 1
self.h, self.m = self.h-dh, self.m-dm
```

4. backtrack for other possible branch for this depth
```python
# this bit is turned off
backtrack(start + 1)
```
note that sometimes this is done by for loop, if there are many branches for this depth
