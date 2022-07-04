'''
15' but spent a long time to figure out the solution
good to implement inorder in first take
'''
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        array = []
        def inorder(node):
            if node.left:
                inorder(node.left)
            array.append(node)
            if node.right:
                inorder(node.right)
        
        inorder(root)
        
        diff = []
        for i in range(1, len(array)):
            if array[i-1].val > array[i].val:
                diff.append(array[i-1])
                diff.append(array[i])
        
        for i, v in enumerate(sorted(diff, key=lambda x: x.val)):
            if diff[i].val != v.val:
                diff[i].val, v.val = v.val, diff[i].val
                return
                
        