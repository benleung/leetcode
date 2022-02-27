'''
about 30'
one take pass
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.maxAvg = 0
        
        def dfs(node):
            if not node:
                return (0,0)
            if not node.left and not node.right:
                self.maxAvg = max(node.val, self.maxAvg)
                return (node.val, 1)
            
            total, count = node.val, 1
            leftTotal,leftCount = dfs(node.left)
            rightTotal,rightCount = dfs(node.right)
            
            total += leftTotal+rightTotal
            count += leftCount+rightCount
            
            self.maxAvg = max(self.maxAvg, total/count)
            
            return (total, count)
        dfs(root) 
        
        return self.maxAvg
