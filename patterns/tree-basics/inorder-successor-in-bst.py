'''
technique of findCanddiate
'''

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.candidate = None # TreeNode
        
        def findCandidate(node): # node is not None
            if node.val > p.val:
                self.candidate = node
                if node.left:
                    findCandidate(node.left)
            else:
                if node.right:
                    findCandidate(node.right)
                
        
        findCandidate(root)
        
        return self.candidate
