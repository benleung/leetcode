'''
11' (after looking at hints)

bad
- mistake on copy paste and didn't change 1->2
- not familiar with inorder (knowledge or converting tree to sorted list)
- 
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = self.inorder(root1)
        list2 = self.inorder(root2)
        return self.sortedMerge(list1, list2)
    
    def sortedMerge(self, list1, list2):
        i = 0
        j = 0
        ans = []
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                ans.append(list1[i])
                i += 1
            else:
                ans.append(list2[j])
                j += 1
        ans += list1[i:] + list2[j:] # rest of elements
        return ans
    
    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root is not None else []
