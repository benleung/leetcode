# basics
subarray means consecutive

# technique 1
- `sumOf(i,j) = sumOf(0,j) - sumOf(0,i-1)`
- however `sumOf(0,j) = ?` needs special handling

# technique 2
- `dp[prefixSum] = i` <- use prefix sum as key in dp, index/bool as value (similar skill in two sums)
example: continuous-subarray-sum

# technique 3: combo chain
example: maximum-product-subarray
- consider things that can disrupt the combo chain
  - zero
  - negative
- solution: keep a variable of xxx_so_far

# technique 4: prefix sum (counting element)
example: flip-string-to-monotone-increasing

nums 0 0 1 1 0
dp   0 0 0 1 2 2

dp[i] = count of 1 of 0..i-1

technique for prefix sum counting
```python
P.append(P[-1] + int(x))
```

with this method, we can know the number of 0/1 on the left/right at all index
