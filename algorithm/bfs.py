def findShortedPath(graph, start, goal):
  explored = []
  queue = [[start]]

  if start == goal:
    return

  while queue:
    path = queue.pop(0) #queue
    node = path[-1]

    if node not in explored:
      neighbours = graph
