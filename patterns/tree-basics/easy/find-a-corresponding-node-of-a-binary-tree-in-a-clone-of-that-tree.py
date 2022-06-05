# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
7'
'''
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(o, c):
            if o == target:
                return c
            else:
                if o.left:
                    result = dfs(o.left, c.left)
                    if result:
                        return result
                if o.right:
                    result = dfs(o.right, c.right)
                    if result:
                        return result
                return None
        return dfs(original, cloned)
