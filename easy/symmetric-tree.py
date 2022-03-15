'''
revisited on 3/8
2'
'''
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def isMirror(left, right):
            if left == None and right == None:
                return True
            elif left == None or right == None:
                return False
            
            if left.val != right.val:
                return False
            
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        return isMirror(root.left, root.right)

'''
revisited on 2/24, worth try one more time
bfs iteration

learn
- order in proper way
- pair by pair
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        q = deque([root.left, root.right])
        while len(q) != 0:
            nextQ = deque()
            
            l = q.popleft()
            r = q.pop()

            while len(q) != 0:
            
                if l and r:
                    if l.val != r.val:
                        return False
                    nextQ.append(l.left)
                    nextQ.append(l.right)
                    nextQ.append(r.left)
                    nextQ.append(r.right)
                elif not l or not r:
                    # only one is None
                    return False
                else:
                    # both None, do nothing
                    pass
                    
            q = nextQ
                
                
            
        
        return True

'''
revisited on 2/24, worth try one more time
21' 

learn
- use ^(xor) wisely -> not only applicable to bit manipulation
- 

'''
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        
        def helper(l, r):
            # itself
            if (l != None) ^ (r != None):
                return False
            if (l == None) and (r == None):
                return True

            if l.val != r.val:
                return False
            # children
            if not helper(l.left, r.right):
                return False
            if not helper(l.right, r.left):
                return False
            return True
        
        if not root:
            return True
        
        return helper(root.left, root.right)

# turns out to be exactly same as the model answer
# 30min

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isSame(root.left, root.right)
    def isSame(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        isOutterSame = self.isSame(root1.left, root2.right)
        if not isOutterSame:
            return False
        isInnerSame = self.isSame(root1.right, root2.left)
        if not isInnerSame:
            return False
        return True
