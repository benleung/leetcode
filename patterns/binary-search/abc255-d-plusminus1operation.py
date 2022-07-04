'''
binary search good questions on accumulative chart
https://atcoder.jp/contests/abc255/tasks/abc255_d

tips: understand the critical points

'''

from math import factorial
import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")

def get_int():
  return int(input())

def get_ints():
  return list(map(int, input().split(' ')))

def get_int_grid(n):
  return [get_ints() for _ in range(n)]

def get_str():
  return input().strip()

def get_strs():
  return get_str().split(' ')

def comb(n,r):
  return factorial(n) // factorial(r) // factorial(n-r)

inf = float("inf")

# solution here
N, Q = get_ints()
array = get_ints()
array.sort()
array.append(inf)
left = [0]*(N+1)
right = [0]*(N+1)

def binary_serach(x): # return index
  l, r = 0, N
  while True:
    center = (l+r)//2
    if x <= array[center] and (center == 0 or x > array[center-1]):
      return center
    elif x > array[center]:
      l = center+1
    else:
      r = center-1

for i in range(2, N+1):
  left[i] = left[i-1] + (i-1)*(array[i-1]-array[i-2])

for i in range(N-2, -1, -1):
  right[i] = right[i+1] + (N-i-1)*(array[i+1]-array[i])

def left_var(index):
  if index == 0:
    return 0
  return index*(x-array[index-1])

def right_var(index):
  if N-index == 0:
    return 0

  return (N-index)*(array[index]-x)

def query(x):
  index = binary_serach(x)
  return left[index] + right[index] + left_var(index) + right_var(index)

for _ in range(Q):
  x = get_int()
  print(query(x))
