# turns out to be exactly same as the model answer
# 30min

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isSame(root.left, root.right)
    def isSame(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        isOutterSame = self.isSame(root1.left, root2.right)
        if not isOutterSame:
            return False
        isInnerSame = self.isSame(root1.right, root2.left)
        if not isInnerSame:
            return False
        return True
