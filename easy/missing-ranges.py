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
