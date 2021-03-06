# The Framework
1. A function or data structure that will compute/contain the answer to the problem for every given state.

- can be indirectly assists finding out solution (e.g. arithmetic slices)
- can be the answer itself (dp[..])

2. recurrence relation to transition between states
e.g. dp(i) = dp(i - 1) + dp(i - 2)

3. base cases,  that our recurrence relation doesn't go on infinitely
dp[1] = ...


# multidimensional dp


# top-down
```python
class Solution:
    def rob(self, nums: List[int]) -> int:

        def dp(i: int) -> int:   # top-down use recursion instead of array
            # Base cases
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])
            
            if i not in memo:
                # Use recurrence relation to calculate dp[i].
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
            
            return memo[i]
        
        memo = {}
        return dp(len(nums) - 1)
```

# bottom-up


# optimized dp space complexity


# common quiz questions
- maximum or minimum of somthing is very common
- Divide and conquer approaches can be parallelized while dynamic programming approaches cannot.

# stone game
- change the game so that whenever Bob scores points, it deducts from Alice's score instead
  - useful techniques for 2 player game
- front-end -> `dp[i][j]` to represent `piles[i], piles[i+1], ..., piles[j]`
- depth can be deduced from i, j, N
