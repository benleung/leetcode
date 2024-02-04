'''
worth revising
'''
from math import factorial
import sys
sys.setrecursionlimit(10**6)

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
N = get_int()
sx, sy, tx, ty = get_ints()
unvisiteds = set(range(N))

circles = []
for _ in range(N):
  circles.append(get_ints())

def distance(coord1, coord2):
  (x1, y1) = coord1
  (x2, y2) = coord2
  return (x1-x2)**2 + (y1-y2)**2   # tips 1: don't take sqrt

def isOnCircle(circle, coord):
  return distance(coord, (circle[0], circle[1])) == circle[2]**2

def areConnectedCircles(node1, node2):
  circle1 = circles[node1]
  circle2 = circles[node2]
  dist = distance((circle1[0], circle1[1]), (circle2[0], circle2[1]))
  return (dist <= (circle1[2] + circle2[2])*(circle1[2] + circle2[2])) and ((circle1[2] - circle2[2])*(circle1[2] - circle2[2]) <= dist)

def sol():

  src = None
  for i, circle in enumerate(circles):
    if isOnCircle(circle, (sx, sy)):
      src = i
      break
  else:
    return False

  dest = None
  for i, circle in enumerate(circles):
    if isOnCircle(circle, (tx, ty)):
      dest = i
      break
  else:
    return False

  def dfs(node):
    if node == dest:
      return True
    
    for unvisited in list(unvisiteds).copy():
      if areConnectedCircles(unvisited, node):
        if unvisited in unvisiteds:  # missing this lead to error
          unvisiteds.remove(unvisited)
          if dfs(unvisited):
            return True

    return False

  unvisiteds.remove(src)
  return dfs(src)

if sol():
  print("Yes")
else:
  print("No")
