'''
2/24 revisited
10'

dfs (recursive)
'''
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, preSum): # preSum exclusive for node, node cannot be None
            curSum = (preSum<<1) + node.val
            if not node.left and not node.right:
                return curSum
            ans = 0
            if node.left:
                ans += dfs(node.left, curSum)
            if node.right:
                ans += dfs(node.right, curSum)
            return ans
                
        # root cannot be None    
        
        return dfs(root, 0)

'''
10'

dfs (recursive)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(0, root)
        return self.ans
        
    def dfs(self, cur, root):
        if root.left == None and root.right == None:
            self.ans += (cur<<1) + root.val   # cur<<1 + root.val doesn't work
        
        if root.left != None:
            self.dfs( ((cur<<1) + root.val), root.left)
        if root.right != None:
            self.dfs( ((cur<<1) + root.val), root.right)


'''
20'

dfs (recursive)

- use stack for dfs
- previous path info attached with node in form of tuple <- new

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0

        st = [(root, 0)] # (node, previous number for the node)
        while st != []:
            (node, cur) = st.pop()
            cur = (cur << 1) | node.val
            if node.left == None and node.right == None:
                ans += cur
            if node.right != None:
                st.append((node.right, cur))
            if node.left != None:
                st.append((node.left, cur))
        return ans
