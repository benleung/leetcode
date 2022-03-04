'''
solution
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and
                   validate(node.left, low, node.val))

        return validate(root)

'''
20'
passing information from child to parent ( trhough return value) is not as good as passing info from parent to child through function parameter
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root): # (minVal, maxVal isValid)
            minVal = root.val
            maxVal = root.val
            isValid = True
        
            if root.left:
                minValLeft, maxValLeft, isValidLeft = helper(root.left)
                minVal = min(minVal, minValLeft)
                maxVal = max(maxVal, maxValLeft)
                
                if not (maxValLeft < root.val):
                    isValidLeft = False
                
                isValid = isValid and isValidLeft
            if root.right:
                minValRight, maxValRight, isValidRight = helper(root.right)
                minVal = min(minVal, minValRight)
                maxVal = max(maxVal, maxValRight)
                
                if not (minValRight > root.val):
                    isValidRight = False
                
                isValid = isValid and isValidRight
                
            return (minVal, maxVal, isValid)
            
        if root.left:
            minVal, maxVal, isValid = helper(root.left)
            if not (maxVal < root.val) or not isValid:
                return False
        if root.right:
            minVal, maxVal, isValid = helper(root.right)
            if not (minVal > root.val) or not isValid:
                return False
            
        return True
