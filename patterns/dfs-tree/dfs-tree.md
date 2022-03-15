# dfs by recursion (best)
example: path-sum
```python
class Solution(object):
    def hasPathSum(self, root, targetSum): # point 1
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            # initial root is empty only if root is empty at the beginning
            return False
        if not root.left and not root.right:    
            # point 2
            return targetSum == root.val
        if root.left and self.hasPathSum(root.left, targetSum-root.val):
            return True
        if root.right and self.hasPathSum(root.right, targetSum-root.val):
            return True
        
        return False
```

## step 1: 
try to divide into subproblem by looking at different children

## step 2: 
- arrange parameter
  - `node` which is a must for tree. define whether it could be null (non-nullable is easy to handle)
  - anything (e.g. `targetSum`) that is required divide the subproblem (by considering the parent node that is already explored) -> not required if not information is needed from parent

## step 3: 
- terminal condition (return value method used here, from backtracking note)
  - `not node.left and not node.right` is a common condition (reach the end of leaf)


## note:
- should understand that 
```python
if root.left and self.hasPathSum(root.left, targetSum-root.val):
    return True
if root.right and self.hasPathSum(root.right, targetSum-root.val):
    return True
```
means 
- `self.hasPathSum(root.left, targetSum-root.val)` has result when reaching the left's termination condition
- `self.hasPathSum(root.right, targetSum-root.val)` has result when reaching the right's termination condition (same parent as root.left, to be root)


# dfs by interations
example: path-sum

```python
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = [(root, sum - root.val), ]  # point 1
        while stack:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:  # point 2
                return True
            if node.right:
                stack.append((node.right, curr_sum - node.right.val)) # point 3
            if node.left:
                stack.append((node.left, curr_sum - node.left.val)) # point 3
        return False
```

## point 1: attach with previous path info (or node inclusion info)
```python
(root, sum - root.val)  # the "sum - root.val" part

```

## point 2: terminal condition

## point 3: stack
- use stack -> dfs
- `append(node.right)` -> `append(node.left)` implies the order of traversal in dfs manner with left first and right on hold

# technique: side effect and return value at the same time
example : maximum-average-subtree

check whenever return
```python
if not node.left and not node.right:
    self.maxAvg = max(node.val, self.maxAvg)
    return (node.val, 1)
```

# tree with backtrack
path-sum-iii as a good example
