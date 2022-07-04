from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict
from itertools import combinations
from math import comb
from math import factorial

a = [1,2,3,23, 33]

# a need to be sorted

print(bisect_right(a,22))  # if insert 23, where is the index of the new element
# print(bisect_left(a,23))  # if insert 23, where is the index of the new element
# print(bisect_right(a, 3))

# print(bisect(a, 3))

# print(max(a,b))
