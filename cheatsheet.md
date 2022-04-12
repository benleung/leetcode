# syntax for python
- max(square, key = lambda k: square[k])
- cmp_to_key
def mycmp(a, b):
    print("comparing ", a, " and ", b)
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
  
  
print(sorted([1, 2, 4, 2], key=functools.cmp_to_key(mycmp)))

# bit manipulations
carry = (a&b) << 1
sum_without_carry = a ^ b
`x & (x - 1)` remove the least significant bit
-x = ~x + 1
mask = 0xFFFFFFFF
x = x & mask
~(a ^ mask)
`x & (-x)` is a way to keep the rightmost 1-bit and to set all the other bits to 0


# 2-d matrix
- Rotate: technque of Rotate Groups of Four Cells (rotate-image)
- Positive diagonal: ↗️ r+c
  - 0...N
  - center: (N//2)*2
- Negative diagonal: ↘️ r-c
  - -(N-1)...(N-1)
  - center: 0
# 2-pointer
  - left < right
  - one for read, one for write
# bfs-matrix
- column number
  - start with 0
  - q.append((n.left, 2*col))
  - q.append((n.right, 2*col + 1))

# dfs-backtrack
- reusing index/depth to filter out some choices are common

# dfs-tree
- prefix sum
  - `h[curPrefix] = True`
  - `h[target-curPrefix]`
# n-sum
- `(a + b)%60 == 0 -> a%60 == (60-b)%60`

# sliding-window
- longest-xxxx-substring always think about whether sliding window can be applied
- shortest-xxx-substring is similar

# subarray
- prefix sum with modulus
```python
(cur - pre) %k = target
implies
(cur - target) %k = pre %k
```

# subsets-combinations-permutations
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

# dynamic programming
- dp-knapsack-01
  - method of all combinations
  - Tabulation 2-D array (meaning of i,j,d[i][j]) _should revise, easy forget after 2 days (forget again on march 8)..._
  - use or not use -> formula (or)
  - `i`
    - items[0]...items[i-1] being explored  (i = 0 means the state of no items)
  - `j` (not something usually used for index)
    - for knapsack, this is "weight"
    - for partition-equal-subset-sum, this is "subset sum"
  - value of `dp[i][j]`
    - for knapsack, this is $
    - for partition-equal-subset-sum, this is True/False
    - usually something requested from the question


- dp-knapsack-unbounded
  - `j` (not something usually used for index)
    - for coin-change, this is total value of coins
  - `dp[j]`
    - match with question (number of coins)

- dp basic
  - dp[i] to represent combinations that last end index is i (should revisit again) arithmetic-slices
  - dp-jump

- dp-lis
  - lis
    - O(N^2) solution, using last end index i
    - `dp[i] = max(dp[i], dp[i+j] + 1)`
    - the optimal solution is however, without using dp, but intelligently build an array with binary search
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

# bit manipulations


- math
  - digital root (too rare)
- dfs-basics
  - iteration: use stack
- tree-basics
  - O(n) for finding height
  - O(n) for finding binary search tree, unless the tree is balanced
  - array implementation of Tree (without dummy head)
    - children at indices 2i + 1 and 2i + 2 
    - its parent floor((i − 1) ∕ 2)
  - array implementation of Tree (with dummy head)
    - children at indices `2i` and `2i + 1`
    - its parent `i∕/2`
  - binary search tree
    - insert by recursion
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
  - check whether valid tree graph-valid-tree (parent hash)

- bfs-tree
  - symmetric-tree can be solved by bfs
    - order the queue in a proper way (populating-next-right-pointers-in-each-node)
  - technique of using queue to transverse (mutliple loop, attach value, order, check None)


- fibonacci
  - without dp, time complexity is O(2^n). 
  - optimize dp space, by rolling prev/cur

- linked list
  - fixed head
    - remove-duplicates-from-sorted-list
  - variable head
    - reverse-linked-list
  - lru: should use doubly linked list


- backtrack
  - general approach
    - terminal
    - reject
    - add condidate -> clean up
    - branches
  - terminal (side effect, return)
  - revisit (inplace, revisit storage)
  - often use "index" for backtrack increment

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





- rotate-arraty
  - use reverse sort twice

- dfs island

- dfs graph
  - create graph (all directly/indirectly connect)
  - traversal with dfs (avoid revisit, action for cluster, stack, explore next, try all node)

- dfs tree
  - recursive
    - imagine about how to traverse
    - terminal condition of `not node.left and not node.right`)
  - iterations

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
  - trie is perfect for word search (Boggle problem)

- priority-queue

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



# easy techniques
- for Elementary Math, use carry, but dun forget last carry
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
while pile>0:
    hour += 1
    pile -= speed

# common careless mistake
- "".join expect each element to be str
- edge cases of 0, empty array, negative
- range(N), upper limit is exclusive (doesn't include N)
- when adding node to queue/stack in tree, think about whether it's None
- when running loop, be careful about the index variable, whether wrongly used the outer one
- remove leading 0, but keep 0 if only one 0 left
- can i use the same element more than once
- forgetting to add visited before initial
- be careful of order of execution, when modifying index
  ```python
  ch_count_in_window[s[l]] -= 1
  l += 1
  ```
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
