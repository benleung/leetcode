'''

'''
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def dfs(node,string):
            if not node:
                string += 'None,'
            else:
                string += "{0},".format(node.val)
                string = dfs(node.left, string)
                string = dfs(node.right, string)
            return string

        return dfs(root, '')        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def dfs(arrays):
            element = arrays.popleft()
            if element == "None":
                return None

            root = TreeNode(element)
            root.left =  dfs(arrays)
            root.right =  dfs(arrays)
            return root
        
        arrays = deque(data.split(','))
        arrays.pop() # remove the trailing ""
        root = dfs(arrays)
        return root
