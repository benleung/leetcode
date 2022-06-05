# Feature to judge
- contiguous subarrays
- substring
- find size of shortest/longest subarray that ...
- O(N) to solve

# Pattern 1: adjust window size to enable window content to fit window requirement
e.g.
```python
def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
  ans = 0
  
  window_size = 0
  cur_prod = 1
  
  for i in range(len(nums)):
      cur_prod *= nums[i]
      window_size += 1
      
      while window_size > 0 and cur_prod >= k:  # point 3
          cur_prod /= nums[i-window_size+1]
          window_size -= 1
      
      ans += window_size
  
  return ans
```


## point 1: substring that ends with xxx
number of combinations = window size

## point 2: left
`left = i-window_size+1`

## point 3: while loop


# Pattern 2: fixed window size
initialize window size
`for i in range(win_size,...)`
`left = i-window_size+1`
