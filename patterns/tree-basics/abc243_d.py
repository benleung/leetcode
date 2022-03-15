'''
30'
'''
import sys
from collections import defaultdict

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

# solution here
N, x = get_ints()
S = get_str()
array = []

for s in S:
  if s == "U" and array and array[-1] != 'U':
    array.pop()
  else:
    array.append(s)

for s in array: 
  if s == 'U':
    x = x >> 1
  elif s == 'L':
    x = x << 1
  elif s == 'R':
    x = (x << 1) + 1

print(x)
