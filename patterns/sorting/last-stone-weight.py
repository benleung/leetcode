'''
9'30"
used heap here, but bucket sort is a even faster solution
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        def heappop():
            return -heapq.heappop(heap)
            
        def heappush(item):
            heapq.heappush(heap, -item)
        
        for stone in stones:
            heappush(stone)
        
        while len(heap) >= 2:
            new_stone = abs(heappop() - heappop())
            if new_stone >0:
                heappush(new_stone)
                
        return heappop() if heap else 0
        