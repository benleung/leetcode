# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 9'
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        return self.findDepth(root, 0)
        
    def findDepth(self, root, depth):
        if root.left == None and root.right == None:
            return depth + 1
        elif root.left == None:
            return self.findDepth(root.right, depth + 1)
        elif root.right == None:
            return self.findDepth(root.left, depth + 1)
        else:
            return min(self.findDepth(root.left, depth + 1), self.findDepth(root.right, depth + 1))
