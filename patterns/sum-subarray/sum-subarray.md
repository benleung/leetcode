# technique 1
- `sumOf(i,j) = sumOf(0,j) - sumOf(0,i-1)`
- however `sumOf(0,j) = ?` needs special handling

# technique 2
- `dp[prefixSum] = i` <- use prefix sum as key in dp, index/bool as value (similar skill in two sums)
