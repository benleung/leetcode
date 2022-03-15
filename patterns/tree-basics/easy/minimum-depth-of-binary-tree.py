'''
revisited on 3/12 6'
careless about a case
'''
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.left:
            return 1 + self.minDepth(root.left)
        elif root.right:
            return 1 + self.minDepth(root.right)
        else:
            return 1

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
