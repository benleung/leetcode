# 2D DP Array is used

`dp[i][j]`

- `i`
  - items[0]...items[i-1] being explored  (i = 0 means the state of no items)
- `j` (not something usually used for index)
  - for knapsack, this is "weight"
  - for partition-equal-subset-sum, this is "subset sum"
- value of `dp[i][j]`
  - for knapsack, this is $
  - for partition-equal-subset-sum, this is True/False
  - usually something requested from the question

- the keep point is relationship of `j` to `dp[i][j]`
  - for knapsack, this is weight -> $
  - for partition-equal-subset-sum, this is subset-sum -> True/False

# Formula
```python
dp[i][j] = \
   dp[i-1][j] or \ # doesn't use this element
   (j >= nums[i-1] and dp[i-1][j-nums[i-1]]) # use this element
```

# Initial

# Transversal
