
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
