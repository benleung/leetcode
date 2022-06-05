'''
2'
'''
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        elif val < root.val and root.left:
            return self.searchBST(root.left, val)
        elif val > root.val and root.right:
            return self.searchBST(root.right, val)
        return None
