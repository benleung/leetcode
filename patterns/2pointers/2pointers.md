# Features
- moving towards each other

# Techniques
- one from left end, one from right end

### Micro

initial condition:

```python
left = 0
right = len(nums)-1
```

terminal condition

```python
while left <= right:
```

iteration (with condition)

```python
# condition for iterations
if .. < .:
	left += 1
if .. < .:
	right -= 1
if ...:
```

iteration (without condition)

```python
left += 1
right += 1
```

# complexity
O(n)
sorting algorithm is usually O(nlogn)

# Pattern 1: One for read, one for write
