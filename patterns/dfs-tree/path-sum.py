# 16min

'''
recursion version
'''
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

'''
iterations

key: 
- use stack instead of queue
'''
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:  
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False
