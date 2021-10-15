# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        toReturn = []
        if root == None:
            return
        self.inorderTraversalRe(root.left, toReturn)
        toReturn += [root.val]
        self.inorderTraversalRe(root.right, toReturn)
        return toReturn
    def inorderTraversalRe(self, root, array):
        if root == None:
            return
        self.inorderTraversalRe(root.left, array)
        array += [root.val]
        self.inorderTraversalRe(root.right, array)
