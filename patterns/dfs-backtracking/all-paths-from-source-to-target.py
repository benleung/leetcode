'''
9'40"
very classic example of backtracking

good
- if solution requires all possible paths instead of just one, use a global variable and let the recursive function to modify it (sol in this example)

learning
- array to represent path (from 0 to N)
  - graph[0] = [1,2] to represent 0->1,0->2

bad
- careless mistake (path instead of  + [target])
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        sol = []
        self.dfs([], 0, graph, sol)
        return sol

    def dfs(self, path, target, graph, sol):
        if target == len(graph)-1:
            sol.append(path + [target])  # had mistake here (path instead of  + [target])
            return
        for nex in graph[target]:
            self.dfs(path + [target], nex, graph, sol)

### secodn solution: not using path + [target]
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        sol = []
        self.dfs([], 0, graph, sol)
        return sol

    def dfs(self, path, target, graph, sol):
        if target == len(graph)-1:
            sol.append(path + [target])
            return
        for nex in graph[target]:
            path.append(target)  ## not using path + [target]
            self.dfs(path, nex, graph, sol)
            path.pop()  ## not using path + [target]
