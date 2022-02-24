'''
revisited on 2/24
5'
trick in understanding what is "left leave" (dun get into recu)
  if root.left.left == None and root.left.right == None:
    count+= root.left.val
'''
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # root is None
        count = 0
        
        if root == None:
            return 0
        if root.left:
            if root.left.left == None and root.left.right == None:
                count+= root.left.val
            else:
                count+= self.sumOfLeftLeaves(root.left)
        count+= self.sumOfLeftLeaves(root.right)
        
        return count


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = 0
        
        if root.left != None:
            if root.left.left == None and root.left.right == None:
                s += root.left.val
            else:
                s += self.sumOfLeftLeaves(root.left)
        if root.right != None:
            s += self.sumOfLeftLeaves(root.right)
        return s
