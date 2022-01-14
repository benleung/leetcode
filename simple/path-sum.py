# 16min

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            # initial root is empty only if root is empty at the beginning
            return False
        if not root.left and not root.right:    
            # leaf is reached
            return targetSum == root.val
        if root.left and self.hasPathSum(root.left, targetSum-root.val):
            return True
        if root.right and self.hasPathSum(root.right, targetSum-root.val):
            return True
        
        return False
