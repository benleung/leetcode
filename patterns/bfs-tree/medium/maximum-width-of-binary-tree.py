'''
after know hints (worth revision)
- column information can be attached (parent related)
- formula for caluclating column
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1
        q = deque([(root, 0)])
        while q:      
            
            # if len(q) > 0:
            ans = max(ans, q[-1][1] - q[0][1] + 1) 
            
            for i in range(len(q)):
                (n, col) = q.popleft()
                if n.left:
                    q.append((n.left, 2*col))
                if n.right:
                    q.append((n.right, 2*col + 1))
        return ans
