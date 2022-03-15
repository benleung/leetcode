'''
30'

bad:
had mistake on order
'''
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        (root, 0)
        
        (root.left, -1)
        (root.right, 1)
        
        result = defaultdict(list)  # {0: [root.val]}
        
        '''
        result = defaultdict(deque)
        
        inf = float("inf")
        self.lo = inf
        self.hi = -inf
        
        if not root:
            return []
        
        queue = deque([(root, 0)])
        while queue:
            node, i = queue.popleft()
            self.lo = min(self.lo, i)
            self.hi = max(self.hi, i)
            result[i].append(node.val)
            if node.left:
                queue.append((node.left, i-1))
            if node.right:
                queue.append((node.right, i+1))
        
        # output result
        ans = []
        self.lo = int(self.lo)
        self.hi = int(self.hi)
        for key in range(self.lo, self.hi+1):
            ans.append(result[key])
        return queue
