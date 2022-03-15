'''
2'40", a very standard question
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        if not root:
            return []
        
        queue = deque([root])
        while queue:
            curLevel = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(curLevel)
        
        return ans
