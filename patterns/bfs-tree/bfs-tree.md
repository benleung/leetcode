# Transversal for each depth
## method 1: multiple loop
example: populating-next-right-pointers-in-each-node
```python
while len(q) > 0:  # point 1
  prev = None  # point 3
  for _ in range(len(q)): # point 1
      node = q.pop()
      node.next = prev
      prev = node
      if node.right:
          q.appendleft(node.right)  # point 2
      if node.left:
          q.appendleft(node.left)  # point 2
```

### point 1
multiple loop

### point 2
- checking whether it's None
- order of pending is important (fifo)

### point 3
operation for this depth

## method 2: append info to a node
(details: WIP)

# column number
q.append((n.left, 2*col))
q.append((n.right, 2*col + 1))
