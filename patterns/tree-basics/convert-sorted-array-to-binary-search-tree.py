'''
less than 10 min
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l, r): # return TreeNode
            if l > r:
                return None
            center = (l+r)//2
            left = dfs(l, center-1)
            right = dfs(center+1, r)
            return TreeNode(val=nums[center], left=left, right=right)
            
        
        return dfs(0, len(nums)-1)

#19'30"

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        middleIndex = int(len(nums)/2)
        rootToReturn = TreeNode(nums[middleIndex])
        rootToReturn.left = self.sortedArrayToBST(nums[:middleIndex])
        rootToReturn.right = self.sortedArrayToBST(nums[middleIndex+1:])
        return rootToReturn
