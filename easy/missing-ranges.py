# 1'30" to understand
# 6' to knwo the solution
# 17' to write the code
# 9' to write for the second time

# 4'20" to finish when known the soution already

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        sol = []
        # rangeItem = []
        # str = 
        
        counter = lower
        numsVar = nums
        
        while numsVar != []:    #  and counter <= upper is unnecessary
            num = numsVar.pop(0)
            if counter == num - 1:
                sol.append(str(counter))
            elif counter < num:
                sol.append("->".join([str(counter),str(num-1)]))
            counter = num + 1
        
        # rest of counter
        if counter < upper:
            sol.append("->".join([str(counter),str(upper)]))
        elif counter == upper:
            sol.append(str(counter))
        
        return sol


'''
2/24
14' to finish for third time (include whiteboarding and understand questions)
'''
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        cur = lower
        sol = [] # [[lower,upper]]
        i = 0
        while i < len(nums):
            if nums[i] == cur:
                i += 1
                cur += 1
            else:  # cur < nums[i]
                sol.append([cur,nums[i]-1])
                cur = nums[i]
        
        # cur -> upper
        if cur <= upper:
            sol.append([cur,upper])
        
        # data massaging on sol for ""->""
        for i,s in enumerate(sol):
            if s[0]==s[1]:
                sol[i] = str(s[0])
            else:
                sol[i] = "{0}->{1}".format(s[0],s[1])
        
        return sol
