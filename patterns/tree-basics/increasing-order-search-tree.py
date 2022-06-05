'''
inorder transversal basics
'''
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        
        self.ans = TreeNode()
        self.cur = self.ans
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.cur.right = node
            self.cur = self.cur.right
            node.left = None
            inorder(node.right)
        
        inorder(root)
        
        return self.ans.right
