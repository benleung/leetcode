# patterns
- math
  - digital root (too rare)
- dfs-basics
  - iteration: use stack
- tree-basics
  - O(n) for finding height
  - O(n) for finding binary search tree, unless the tree is balanced
  - array implementation of Tree
    - children at indices 2i + 1 and 2i + 2 
    - its parent floor((i − 1) ∕ 2)
  - binary search tree
    - insert
  - traversals
    - inorder
      - inorder of BST -> sorted list
    - preorder
    - postorder
  - lowest-common-ancestor
    - check cur.val against p.val and q.val along the traversals, until their destination split off
  - convert list to balanced tree (sort -> preorder transversal)
  - write recursion wisely
    - symmetric-tree (practice)
    - dun call recursion too fast because sometimes cannot distinguish left/right
      - e.g. sum-of-left-leaves
  - lowest-common-ancestor-of-a-binary-tree is a classic problem 
    - solve by dfs-backtracking on tree (but more like recursive)
  - binary tree and binary search tree are different

- bfs-tree
  - symmetric-tree can be solved by bfs
    - order the queue in a proper way (populating-next-right-pointers-in-each-node)
  - technique of using queue to transverse (mutliple loop, attach value, order, check None)
- bfs-matrix
  - shortest path is used
  - bfs from goal(s) or start(s) are possible
  - remember to avoid revisiting
  - attach additional info (depth) 

- fibonacci
  - without dp, time complexity is O(2^n). 
  - optimize dp space, by rolling prev/cur

- linked list
  - fixed head
    - remove-duplicates-from-sorted-list
  - variable head
    - reverse-linked-list

- backtrack
  - general approach
    - terminal
    - reject
    - add condidate -> clean up
    - branches
  - terminal (side effect, return)
  - revisit (inplace, revisit storage)

- bit manipulation
  - counting-bits is a classic problem to memorize
    - `dp[x-offset]`
  - power of two/four
    - and operator on non-power of two/four
    - maximum possible value (check whether exist in hex form, 8 charaters 32 bit)
    - `(x - 1) == 0` if only one bit is present
    - find difference by `^=` (e.g. find-the-difference, single-number)
    - there is formula for carry, without carry

- power-of-three
  - not power-of-2/4 so no bit manipulations available
  - consider the base of 3, and write iteration to check each bit

- linkedlist
  - trick of delete node by swapping value

- 2-d matrix
  - Rotate: technque of Rotate Groups of Four Cells (rotate-image)
  - transpose
  - reflect (dun forget `range(n // 2)`

- 2-pointer
  - left < right
  - one for read, one for write

- rotate-arraty
  - use reverse sort twice

- dfs island

- dfs graph
  - create graph (all directly/indirectly connect)
  - tranversal with dfs (avoid revisit, action for cluster, stack, explore next, try all node)

- dfs tree
  - recursive
    - imagine about how to tranverse
    - terminal condition of `not node.left and not node.right`)
  - iterations

- dp-knapsack-01
  - method of all combinations
  - Tabulation 2-D array (meaning of i,j,d[i][j]) _should revise, easy forget after 2 days..._
  - use or not use -> formula (or)

- dp-knapsack-unbounded
  - index: total value of coins

- dp basic
  - dp[i] to represent combinations that last end index is i (should revisit again) arithmetic-slices
  - dp-jump

- dp-lis
  - lis
    - O(N^2) solution, using last end index i
  - num of lis
    - DP array can store more than one thing by tuple

- dp-house-robber
  - using last end index i
  - decision of include this or not include this


- dp-lcs
  - longest-common-subsequence
    - one index for start, one index for end
    ```python
    if text1[i-1] == text2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1  # had mistake here before
    else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    ```

- dp-matrix
  - trick about maximal-square

- dp-longest-palindromic-substring
  - expanding width between left/right indexes
  - width of 0/1 are special cases

- fast-and-slow-pointer
  - can detect cycle linked list
  - can check where cycle begins -> fast and slow to detect conflict -> both slow

- greedy
  - stack is a good way: remove-k-digits
  - combine element -> transverse from right to left (instead of left to right) can be better a substitute for stack

- nsum
  - 2sum, unsorted: hashtable
  - 2sum, sorted: two pointer
  - 3sum: just a more complicated version of 2sum sorted
  - 4sum: no time to revise

- prefix-tree
  - better sort first before insert

- priority-queue
  - how to build a heap? (to revise in future before interview)

- quickselect
  - revise before interview
  - recursion is used

- sliding-windows
  - rolling hash
  - edit on the same value (+/-)
  - adjust left's pointer when meet bottleneck at right

- sorting
  - revise in future before interview (notion)

- sum-subarray
  - technique: `sumOf(i,j) = sumOf(0,j) - sumOf(0,i-1)`
  - `dp[prefixSum]` <- use prefix sum as index
  - continuous-subarray-sum -> can also train modolus thinking
  - except: left and right product list

- subsets-combinations-permutations
  - subsets
    - cascading (allow duplication)
    - cascading (avoid duplicates)
    - backtrack with counters for all combinations, to avoid duplicates -> backtrack
  - combinations
  - combinations (backtrack with counter, technique to skip unnecessary branches)
  - permutations
    - swapping (allow duplication)
    - backtrack (avoid duplicates)
  - same value of different index, avoid duplication -> counter

# easy techniques
- for Elementary Math, use carray, but dun forget last carry
- smart ways to avoid duplicate -> sort -> compare with last node
- 1-to-1: 2 hashmap is required
- stack is a good datastructure for possibly removing/comparing with last element (e.g. valid-parentheses, backspace-string-compare)
- writing while loop/recursive function
  - remember to iterate (`+=`)
  - dun forget actions to do at terminal condition
  - think what the terminal condition will be
- array index
  - opposite index is `length - 1 - i`
- convert into graph to observe the up and down
- queue
  - appendleft -> pop and append -> popleft has the same result (depends on how to want to visualize)


# common careless mistake
- "".join expect each element to be str
- edge cases of 0, empty array, negative
- range(N), upper limit is exclusive (doesn't include N)
- when adding node to queue/stack in tree, think about whether it's None
- when running loop, be careful about the index variable, whether wrongly used the outer one
- remove leading 0, but keep 0 if only one 0 left
- can i use the same element more than once
- forgetting to add visited before initial

# knowledge on python
- deque.pop(n) is not O(1) (it is a double linked list, only end or front is O(1))
- set
  - `s1 | s2`  not `s1 + s2`
  - `s1 - s2`
- heap
  - `heapq.nlargest(k,nums.keys(), key=nums.get)` array to return
  - `heapq.nsmallest(k, h.keys(), key=lambda word: (-h.get(word), word))`
- dict
  - del h['a']
- `.copy()` deep copy doesn't work for array inside array

# Datastructure Knowledge
- monotonic deque
  - a queue with increasing numbers/decrease numbers
  - useful for storing a list of "the next max number" / "the next min number"

# Other techniques or topics

## technique of O(1) even space is obviously needed
modify the original array

## array to number
- remove-k-digits
- next-permutation
