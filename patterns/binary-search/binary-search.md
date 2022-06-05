# Types of questions
- sorted
- unsorted but look for a peak point
  - as long as you can rule out some part
- the target point need to match with certain conditions (e.g. compare with point nearby)

# Minmax algorithm
example: koko-eating-bananas
- find the min/max candidates, and run binary search
```python
min_k = math.ceil(sum(piles)/h)
max_k = math.ceil(max(piles)/(h//len(piles)))
```
- no terminal condition for success, but has condition to add candidate
