'''
30'
solve by myself
forget in order transversal is the sorted array
'''
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.num = 1
        
        def check_or_increment():
            if self.num == k:
                return True
            else:
                self.num += 1
        
        def dfs(node):
            if node.left:
                res = dfs(node.left)
                if res != None:
                    return res
            if check_or_increment():
                return node.val
            if node.right:
                res = dfs(node.right)
                if res != None:
                    return res
            return None
                
        return dfs(root)
