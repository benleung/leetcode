'''
20'
'''
class Solution:    
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        stack = []
        self.max_depth = 0
        def dfs(depth, nestedInteger): # (depth, value)
            if nestedInteger.isInteger():
                self.max_depth = max(depth, self.max_depth)
                stack.append( (depth, nestedInteger.getInteger()) )
            else:
                for nextInteger in nestedInteger.getList():
                    dfs(depth+1, nextInteger)
            
        for nestedInteger in nestedList:
            dfs(1, nestedInteger)

        ans = 0
        for depth, val in stack:
            ans += (self.max_depth - depth + 1) * val
        return ans
