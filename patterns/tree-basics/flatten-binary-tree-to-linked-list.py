'''
14'
there is also a space O(1) solution that is worth studying
'''

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        
        right = root.right
        left = root.left
        
        root.left = None
        last_element_of_left = root
        if left:
            root.right = left
            last_element_of_left = left
            while last_element_of_left.right != None:
                last_element_of_left = last_element_of_left.right
            
        last_element_of_left.right = right
