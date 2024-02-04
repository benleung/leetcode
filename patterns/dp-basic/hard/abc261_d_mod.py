# https://atcoder.jp/contests/abc261/tasks/abc261_d

'''
- dp for acc sum with mod
  - dp[(acc_sum-cur)%mod] get familiar
  - if there are different mod required, need one more dimension of mod (mod = 1, mod = 2, ....), one dp cna only store one mod
- for loop of 3, 8, 13 (size = 5)
  - dun use j*5-a because it's overcomplicated
  - range(size-a, N, size)
- dun let update of dp by this element affect the calc.
'''

from collections import defaultdict
from math import ceil, factorial
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
mod = 998244353

# solution here
N = get_int()
array = get_ints()

dp = [[[0]*(N) for _ in range(N+1)] for _ in range(N+1)]   # dp [number of digits] [acc sum % N] [mod]
dp[0][0][0] = 1

ans = 0

for i in range(N):
  a = array[i]

    # for j in range((a//size), ceil((N+a)/size)):
    # ans += dp[size-1][(j*size-a)]

  for size in range(2, i+2):
    for j in range(N):
      if (j+a)%size == 0:
        ans += dp[size-1][j][]

  for size in range(i+1, 1, -1):
    for total in range(N):
      dp[size][total][size] += dp[size-1][(total-a)%N][size]
  dp[1][a%N] += 1

  ans += 1
print(ans)
