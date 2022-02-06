'''
16' (a reasonable time if first time to face this problem)

good
- come up with algorithm for intersection
- knows that comparing the endpoiht is the key

bad
- not fast enough for 2 pointers iterating
'''

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i<len(firstList) and j<len(secondList):
            first = firstList[i]
            second = secondList[j]
            
            res = self.intersect(first,second)
            if res != []:
                ans.append(res)
            
            if first[1]<second[1]:#comparing end point is the key
                i += 1
            elif first[1]>second[1]:
                j += 1
            else:
                i += 1
                j += 1
        return ans
    def intersect(self, first, second):
        left = max(first[0],second[0])
        right = min(first[1],second[1])
        
        if left > right:
            return []
        else:
            return [left, right]
