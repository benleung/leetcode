# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# 3'21"


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
5' use iterations for dfs
'''
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        result = 0
        st = []
        if root != None:
            st.append((root, 1))
        while st != []:
            (node, depth) = st.pop()
            result = max(result, depth)
            if node.left:
                st.append((node.left, depth+1))
            if node.right:
                st.append((node.right, depth+1))
        
        return result
