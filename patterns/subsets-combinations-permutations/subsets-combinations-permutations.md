# complexity
- Time complexity: O(N*2^N) to generate all subsets and then copy them into output list.
  - think of decision tree, it would be depth of N, with 2^N branches at the end

- Space complexity: O(N*2^N)
  - This is exactly the number of solutions for subsets multiplied by the number NN of elements to keep for each subset.

For a given number, it could be present or absent (i.e. binary choice) in a subset solution. As as result, for NN numbers, we would have in total 2^N2 
N
  choices (solutions).

# cascading
example: subsets
```python
output = [[]] #initial

for num in nums:
    output += [curr + [num] for curr in output]  # writing in one line is a smart way to avoid problem
```

# cascading (iterative)(avoid duplications)
example: subsets-ii
```python
sol = [[]]
nextSubsets =[]
nums.sort()

for i in range(len(nums)):
    isThisNumDuplicate = i>0 and nums[i-1] == nums[i]
    
    if not isThisNumDuplicate:
        nextSubsets = sol.copy()

    for j in range(len(nextSubsets)):
        nextSubsets[j] = nextSubsets[j] + [nums[i]]

    sol += nextSubsets
```

# knowledge to know
Heap's algorithm can produce all possible permutations of n objects

# Careless
- same number but from different index -> duplicates
- different order -> duplicates?
- empty set is also considered?
