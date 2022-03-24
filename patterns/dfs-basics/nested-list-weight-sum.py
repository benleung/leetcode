'''
4'40"
recursive thinking is good
'''
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, depth):
            total = 0
            for integer in nestedList:
                if integer.isInteger():
                    total += depth*integer.getInteger()
                else:
                    total += dfs(integer.getList(), depth+1)
            return total
        return dfs(nestedList, 1)

'''
1 hr
think too much about stack
'''
class Solution:
    
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.ans = 0

        def helper(depth, nestedInteger):
            if nestedInteger.isInteger():
                self.ans += nestedInteger.getInteger()*depth
            else:
                for nestedInteger in nestedInteger.getList():
                    helper(depth+1, nestedInteger)
        
        for nestedInteger in nestedList:
            helper(1, nestedInteger)
        
        return self.ans
