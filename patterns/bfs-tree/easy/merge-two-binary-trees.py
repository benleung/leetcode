'''
11'

good
- one time pass
- think of handling using optional chain mindset
- careful about terminal condition

learn
- bfs is also possible -> try next time if have chance

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root1 == None and root2 == None:
            return None
        
        val = 0
        root1Left, root1Right, root2Left, root2Right = None, None, None, None
        if root1:
            val += root1.val
            root1Left = root1.left
            root1Right = root1.right
        if root2:
            val += root2.val
            root2Left = root2.left
            root2Right = root2.right
        
        left = self.mergeTrees(root1Left, root2Left)
        right = self.mergeTrees(root1Right, root2Right)
        
        head = TreeNode(val, left, right)
        return head
