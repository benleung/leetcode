# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path_to_start = [root.val]
        path_to_end = [(root.val, "")]
        reverseIndex = {}
        ans = []
        
        def dfs_to_start(node):
            if node.val == startValue:
                return True # found

            if node.left:
                path_to_start.append(node.left.val)
                if dfs_to_start(node.left):
                    return True
                path_to_start.pop()

            if node.right:
                path_to_start.append(node.right.val)
                if dfs_to_start(node.right):
                    return True
                path_to_start.pop()
            
            return False
        
        
        def dfs_to_end(node):
            if node.val == destValue:
                return True # found

            if node.left:
                path_to_end.append((node.left.val, 'L'))
                if dfs_to_end(node.left):
                    return True
                path_to_end.pop()

            if node.right:
                path_to_end.append((node.right.val, 'R'))
                if dfs_to_end(node.right):
                    return True
                path_to_end.pop()
            
            return False
        
        dfs_to_start(root)
        
        dfs_to_end(root)
        
        for index, val in enumerate(path_to_end):
            reverseIndex[val[0]] = index
        
        
        while path_to_start[-1] not in reverseIndex:
            ans.append('U')
            path_to_start.pop()
        
        for i in range(reverseIndex[path_to_start[-1]]+1, len(path_to_end)):
            _, direction = path_to_end[i]
            ans.append(direction)
            
        return "".join(ans)
        