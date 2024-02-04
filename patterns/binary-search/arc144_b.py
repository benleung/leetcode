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
N, a, b = get_ints()
arr = get_ints()
arr.sort()
h = {}

def isOK(x):
  if x in h:
    return h[x]
  left = 0
  right = len(arr)-1
  lo = arr[left]
  hi = arr[right]


  while left < right:
    # print("ho")
    left_count = (x-lo+a-1) // a if x >= lo else 0
    right_count = (max(hi-x, 0)) // b
    # print(left_count)
    # print(right_count)
    # print("====")
    count = min(left_count, right_count)

    if left_count == 0:
      break

    if left_count == count:
      left += 1
      lo = arr[left]
    else:
      lo += a*count

    if right_count == count:
      right -= 1
      hi = arr[right]
    else:
      hi -= b*count
  result = lo >= x
  h[x] = result
  return result


def binary_search(lo, hi):
  while lo < hi:
    mid = (lo+hi)//2
    # print(mid)
    # print(isOK(mid))
    # print(isOK(mid+1))
    if isOK(mid) and not isOK(mid+1):
      return mid
    elif not isOK(mid):
      hi = mid-1
    else:
      lo = mid + 1
  else:
    return lo

print(binary_search(arr[0], arr[-1]))
