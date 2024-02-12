'''
17'
revise on 4/10, careless on h[0] = 1

20'
prefix sum
backtrack in tree
'''
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        h = defaultdict(int) # prefix sum -> # of this sum
        self.ans = 0
        h[0] = 1  # revised on 2024/2/11, didn't miss this
        
        if not root:
            return 0
            
        def backtrack(node, accSum):
            accSum += node.val
            self.ans += h[accSum - targetSum]

            h[accSum] += 1  # revised on 2024/2/11, good to recall that i should write in this way
            if node.left != None:
                backtrack(node.left, accSum)
            if node.right != None:
                backtrack(node.right, accSum)
            h[accSum] -= 1
            
        backtrack(root,0 )
        
        return self.ans
