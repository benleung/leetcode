# low priority
math
bit-manipulation

# tree basics
- array implementation of Tree (without dummy head)
  - children at indices 2i + 1 and 2i + 2 
  - its parent floor((i − 1) ∕ 2)
- array implementation of Tree (with dummy head)
  - children at indices `2i` and `2i + 1`
  - its parent `i∕/2`

# list of methods
- recursion
- backtrack
- bfs-matrix
- linkedlist
- 2 pointer
- dfs graph
- dp-knapsack-01
- dp-knapsack-unbounded
- dp-basics
  - combinations that last end index is i
  - house-robber
  - max/min of a subset
  - imagine the final status (flip-string-to-monotone-increasing, trapping-rain-water)
  - calc for each index (trapping-rain-water)
  - if backtracking is necessary, at least try memorization (target-sum)
- dp-lis
  - n^2 sol for dp (loop on dp)
- stack
- sliding window
- subsets-combinations-permutations
  - cascading
  - backtracking
  - swap
- subarray
  - combo chain
  - continuous-subarray-sum (prefix sum)
  - `dp[prefixSum] = i` <- use prefix sum as key in dp, index/bool as value
- longest increasing subsequence (intelligently build subsequence)
- prefix-tree
- monotonic deque
  - binary search (bisect)
- heap
  - double heap for median
  - largest k elements (minheap)
  - smallest k elements (maxheap)
- greedy
  - gas-station
- graph
  - prerequisites -> stack (last append first)

# syntax
- sorted(map(str, nums), key=cmp_to_key(cmp), reverse=True)
```
def mycmp(a, b):
    print("comparing ", a, " and ", b)
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
```
- bisect_left(array, val)
  - all(val < x for val in a[lo : i]) for the left side and all(val >= x for val in a[i : hi]) for the right side
- array.insert(index, val)
- `s1 | s2`
- `heapq.nlargest(k,nums.keys(), key=nums.get)`
- set(combinations(pages,3))
- set can be dict key



# common careless mistake
- "".join expect each element to be str
- edge cases of 0, empty array, negative
- range(N), upper limit is exclusive (doesn't include N)
- when adding node to queue/stack in tree, think about whether it's None
- when running loop, be careful about the index variable, whether wrongly used the outer one
- remove leading 0, but keep 0 if only one 0 left
- can i use the same element more than once
- forgetting to add visited before initial
- careless about < vs <=

# to memorize
- subsets
  - Time complexity: O(N*2^N) to generate all subsets
  - Space complexity: O(N*2^N)
