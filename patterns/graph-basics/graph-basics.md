# logical deduction
example: find-the-celebrity (a very beautify question)
look at the followining conditions
1. pointed by everyone
2. point at no one
assume that celebrity exists (fulfill both condtions), only one 2. is fulfilled
only O(N) is needed to find that might fulfill both conditions, by eliminating other candidates that cannot fulfill the following necessary conditions
- not pointed by any candidates
- point any candidate
check A -> B
- if true: A is elimated from being the candidate
- if false: B is elimated from being the candidate

# Dijkstra's algorithm
example: network-delay-time

### intro
- shortest path from one point to another other points
- key point for algorithm
  - min-heap is needed
    - accumulated distance
  - bfs
- explaination of algorithm
  - https://www.youtube.com/watch?v=EaphyqKU4PQ



# Minimum Spanning Tree / MST
look at tree-basics
