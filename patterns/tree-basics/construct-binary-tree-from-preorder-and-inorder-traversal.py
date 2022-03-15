'''
fundamental  knowledge about preorder and inorder array
finish in 13' after reading hints
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        
        root_i = -1
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                root_i = i
                break
        
        left_inorder = inorder[:root_i]
        if len(left_inorder) != 0:
            root.left = self.buildTree(preorder[1:1+len(left_inorder)] , left_inorder)
        
        right_inorder = inorder[root_i+1:]
        if len(right_inorder) != 0:
            root.right = self.buildTree(preorder[1+len(left_inorder):1+len(left_inorder)+len(right_inorder)] , right_inorder)
            
        return root
