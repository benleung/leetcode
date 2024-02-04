
'''
solution using union find
'''

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        # parents[i]
        # -1: <0 means i is the representative, 1 element in the tree
        # -2: <0 means i is the representative, 2 elements in the tree
        # 2: >0 means i is not the representative, look at parents[2] for representative

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

class Solution(object):
    
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        R = len(grid)
        C = len(grid[0])
        
        self.node_cur = 0
        self.node_dict = {}
        
        def node_add(r, c):
            self.node_dict[(r, c)] = self.node_cur
            self.node_cur += 1
        
        def get_node(r, c):
            return self.node_dict[(r, c)] if (r,c) in self.node_dict else None
        
        
        
        
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    node_add(i, j)
        
        uf = UnionFind(len(self.node_dict))
        
        for i, j in self.node_dict:
            cur = get_node(i, j)
            top = get_node(i-1,j)
            left = get_node(i,j-1)
            if top != None:
                uf.union(cur, top)
            if left != None:
                uf.union(cur, left)
                
        
        return uf.group_count()
'''
13' 

good
- able write the edge cases for 2-d array well

learn
- learn how to solve without hint
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    num += 1
                    self.dfs(grid, i, j)
        return num   
                
    def dfs(self, grid, i, j):
        if grid[i][j] == "1":
            grid[i][j] = "0"
            
            # 4 directions
            if i>=1:
                self.dfs(grid, i - 1, j)
            if i<=len(grid)-2:
                self.dfs(grid, i + 1, j)
            if j>=1:
                self.dfs(grid, i, j - 1)
            if j<=len(grid[i])-2:
                self.dfs(grid, i, j + 1)
