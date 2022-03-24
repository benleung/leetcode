'''
23'
misudnerstood problem for some time
the transversal code writing was a bit slow
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        # is_reserve for each depth
        # iterative, queue
        # swap left, right if necessary -> add the child into queue
        
        if not root:
            return None
        
        q = deque([root])
        
        is_reverse = False # True: swap is necessary
        ans  = []
        
        while q:
            cur_depth = []
            for _ in range(len(q)):
                if is_reverse:        
                    node = q.pop()
                    cur_depth.append(node.val)
                    
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                else:                    
                    node = q.popleft()
                    cur_depth.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
                
            ans.append(cur_depth)
            is_reverse = not is_reverse
        return ans
