'''
revisit on 4/13: 
16' (a reasonable time if first time to face this problem)

good
- come up with algorithm for intersection
- knows that comparing the endpoiht is the key

bad
- not fast enough for 2 pointers iterating
'''

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        firstptr = 0
        secondptr = 0
        
        def intersection(first, second):
            start = max(first[0], second[0])
            end = min(first[1], second[1])
            return [start,end]
        
        while firstptr < len(firstList) and secondptr < len(secondList):
            first = firstList[firstptr]
            second = secondList[secondptr]
            
            if first[1] < second[0]:
                firstptr += 1
            elif second[1] < first[0]:
                secondptr += 1
            else:
                ans.append(intersection(first,second))
                if first[1] < second[1]:
                    firstptr += 1
                elif second[1] < first[1]:
                    secondptr += 1
                else:
                    firstptr += 1
                    secondptr += 1
        
        return ans

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
