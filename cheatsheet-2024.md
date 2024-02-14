

# careless

## misunderstand question
rewrite the array instead of return a value (game-of-life)
wrong output
>= instead of == or > (minimum-size-subarray-sum)
be careful of leading zero

## used wrong variables
node instead of root
total instead of targetSum (path-sum)
when running loop, be careful about the index variable, whether wrongly used the outer one

## edge cases
Division by zero
rotate-string -> length of string is not the same
case of not target found
  minimum-size-subarray-sum
edge cases of 0, empty array, negative
range(N), upper limit is exclusive (doesn't include N)

## misc
when adding node to queue/stack in tree, think about whether it's None
can i use the same element more than once
forgetting to add visited before initial
def assignNode(node):  # updating `node=xxx` is copy by value only
  
## order of execution, especially when modifying index / sliding window
```
i += 1
hoge(i)
```
vs 
```
hoge(i)
i += 1
```

# syntax for python
cmp_to_key
import functools
def mycmp(a, b): # in order
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
print(sorted([1, 2, 4, 2], key=functools.cmp_to_key(mycmp)))
bisect.bisect_left(array,x)
"".join(ans).lstrip('0') or "0"  # remove leading zeros
- set
  - `s1 | s2`  not `s1 + s2`
  - `s1 - s2`


# math formula
Pascal Triangle: nCr = n!/r!(n-r)!
