'''
mistake: should use r-c intead R-C
<10min
'''
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        R = len(mat)
        C = len(mat[0])
        
        h = defaultdict(list)
        
        
        for r in range(R):
            for c in range(C):
                key = r-c
                heapq.heappush(h[key], mat[r][c])
        for r in range(R):
            for c in range(C):
                key = r-c
                mat[r][c] = heapq.heappop(h[key])

        return mat
