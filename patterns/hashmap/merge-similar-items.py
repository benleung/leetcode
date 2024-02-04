'''
learning: 2d array can use sort()
'''
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        h = defaultdict(int)
        for item in items1:
            h[item[0]] += item[1]
        for item in items2:
            h[item[0]] += item[1]

        return sorted([[val, weight] for val, weight in h.items()])
