'''
learn: how to wrap heap
knowledge about factor
'''
import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        maxheap = []
        
        def heappush(x):
            heapq.heappush(maxheap, -x)
            if len(maxheap) == k + 1:
                heapq.heappop(maxheap)
            
        def heappop():
            return -heapq.heappop(maxheap)
        
        def heapmax():
            return -maxheap[0]
        
        for i in range(1, int(math.sqrt(n))+1):
            if n % i == 0:
                heappush(i)
                if i != n/i:
                    heappush(n//i)
                
        return heapmax() if len(maxheap)==k else -1

'''
kth xxx -> heap is used
5 minutes brute force solution
'''
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # brute force. space 1, time O(n)
        count = 0
        for i  in range(1,n+1):
            if n % i == 0:
                count += 1
            if count == k:
                return i
        return -1
        