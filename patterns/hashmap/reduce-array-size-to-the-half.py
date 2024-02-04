'''
5'
'''

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # [3,3,3,3,5,5,5,2,2,7]
        # 3: 4
        # 5:3
        # 2: 2
        # 7: 1
        counter = Counter(arr)
        sortedList = sorted(counter.values(), reverse=True)
        
        count_to_remove = ceil(len(arr)/2)
        ans = 0
        
        for count in sortedList:
            count_to_remove -= count
            ans += 1
            if count_to_remove <= 0:
                return ans
        
        return ans
