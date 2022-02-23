'''
43'

good:
remember to use the trick of helper function helper(self, curRoutes, root)

problems
- not able to distinguish append and += well
- not able to realize the solution required is an array instead of string, so should use return [...] instead of ...

learnt
- map(lambda r: str(r), routes)


to do next
try to use iteration instead of recursion
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.helper([], root)
    
    def helper(self, curRoutes, root):
        node = root
        newRoutes = curRoutes + [node.val]
        if node.left == None and node.right == None:
            return self.f(newRoutes)
        else:
            sol = []
            if node.left != None:
                sol += self.helper(newRoutes, node.left)
            if node.right != None:
                sol += self.helper(newRoutes, node.right)
            return sol
            
    def f(self, routes):
        return ["->".join(map(lambda r: str(r), routes))]
