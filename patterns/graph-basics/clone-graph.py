'''
careless on forgetting to add visited before initial
37'
'''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        h = {}
        
        if not node:
            return None
        
        def copyNode(n):
            return Node(n.val)
        
        st = [node]
        h[node] = copyNode(node)
        
        
        # h
        while st:
            n = st.pop()
            for neighbor in n.neighbors:
                if neighbor not in h:
                    h[neighbor] = copyNode(neighbor)
                    st.append(neighbor)
        
        ans = h[node]
        
        visited = set()
        
        st = [node]
        visited.add(node)
        while st:
            n = st.pop()
            cur = h[n]
            for neighbor in n.neighbors:
                cur.neighbors.append(h[neighbor])
                if neighbor not in visited:
                    visited.add(neighbor)
                    st.append(neighbor)
        
        return ans
