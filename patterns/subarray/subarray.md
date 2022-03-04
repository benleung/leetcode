# technique 1
- `sumOf(i,j) = sumOf(0,j) - sumOf(0,i-1)`
- however `sumOf(0,j) = ?` needs special handling

# technique 2
- `dp[prefixSum] = i` <- use prefix sum as key in dp, index/bool as value (similar skill in two sums)

# technique 3: combo chain
example: maximum-product-subarray
- consider things that can disrupt the combo chain
  - zero
  - negative
- solution: keep a variable of xxx_so_far
