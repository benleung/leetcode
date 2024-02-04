'''
6' straight-forward bfs
'''

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = deque([root]) if root else []
        while queue:
            N = len(queue)
            for i in range(N):
                node = queue.popleft()
                if N-1 == i:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        
        return ans
