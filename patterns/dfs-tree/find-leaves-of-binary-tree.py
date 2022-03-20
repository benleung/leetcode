'''
30' struggle at what dfs to write
'''
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaves = []
        
        def isLeaf(node):
            return node.left == None and node.right == None
        
        
        def dfs(root):
            # assume root is not None, and is not leave
            bottom_leaves = []
            if root.right:
                if isLeaf(root.right):
                    bottom_leaves.append(root.right.val)
                    root.right = None
                else:
                    bottom_leaves.extend(dfs(root.right))

            if root.left:
                if isLeaf(root.left):
                    bottom_leaves.append(root.left.val)
                    root.left = None
                else:
                    bottom_leaves.extend(dfs(root.left))
            return bottom_leaves
                
        
        while root and not isLeaf(root):
            leaves.append(dfs(root))
        
        leaves.append([root.val])
        
        return leaves
