'''
20'
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # for the following edge case, so my logic doesn't need to assume the max value might be a negative or zero
        # nums only negative or 0
        ans = max(nums)
        
        negCur = None
        posCur = None        
        for n in nums:
            if n == 0:
                negCur = posCur = None
            elif n > 0:
                if posCur != None:
                    posCur *= n
                else:
                    posCur = n
                if negCur != None:
                    negCur *= n
                ans = max(ans, posCur)
            else:
                if negCur != None:
                    negCur *= n # now positive
                if posCur != None:
                    posCur *= n # now negative
                else:
                    posCur = n # now negative (ready to swap)
                negCur, posCur = posCur, negCur
                if posCur != None:
                    ans = max(ans, posCur)
        
        
        return ans
