# topdown approach
# 18' (include thinking for another solution with took 15')

'''
O(nlogn)
'''
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root == None:
            return True
        
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1



'''
second time: O(N) solution
'''
