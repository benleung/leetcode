https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/

# 2'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


# without recursion (simulate recursion using stack)
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []
        
        toProcess = [root]
        stack = []
        
        
        
        while toProcess != []:
            item = toProcess.pop()
            stack.append(item.val)
            if item.left is not None:
                toProcess.append(item.left)
            if item.right is not None:
                toProcess.append(item.right)

        return reversed(stack)
