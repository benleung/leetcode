'''
30' 
spend some time walking from the examples, calculate the values 
-> useful in thinking about the solution, should do this in a faster fashion
since i know the technique of breaking down sub problems...
'''
class Solution:
    def numTrees(self, n: int) -> int:
        d = [0] * (n+1) # half of space can be saved
        d[0] = 1
        for i in range(1, n+1):
            for j in range(1,i+1):
                d[i] += d[j-1]*d[i-j]
        return d[n]
