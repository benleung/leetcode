'''
should revise, not optimal solution
'''


'''
29' code

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        pathP = []
        p = p.val
        q = q.val
        
        cur = root
        while cur:
            pathP.append(cur.val)
            if cur.val == p:
                break
            elif p > cur.val:
                cur = cur.right
            elif p < cur.val:
                cur = cur.left
        
        pre = root
        if root.val == q:
            return root
        cur = root.left if q < root.val else root.right

        for i in xrange(1, len(pathP)):
            if pathP[i] != cur.val:
                return pre
            
            if cur.val == q:
                return cur
            elif q > cur.val:
                pre = cur
                cur = cur.right
            elif q < cur.val:
                pre = cur
                cur = cur.left
        return pre

'''
2/23
17'

not the optimal solution because waste space
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findPath(target):
            cur = root
            path = []
            while True:
                path.append(cur)
                if target > cur.val:
                    cur = cur.right
                elif target < cur.val:
                    cur = cur.left
                else:
                    return path
                
        pPath = findPath(p.val)
        qPath = findPath(q.val)

        minL = min(len(pPath),len(qPath))
        for i in range(minL):
            if pPath[i].val!=qPath[i].val:
                return pPath[i-1]
        else:
            return pPath[minL-1]
