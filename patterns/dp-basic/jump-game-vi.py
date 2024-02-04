'''
should do again
1hr because forget heapq syntax

special about priority queue + sliding window
dp is the optimal solution here: you can let dp[i] represent the max score we can get starting at index i
'''
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap=[]
        def heappush(x, i):
            heapq.heappush(heap, (-x, i))
            
        def heappop():
            res = heapq.heappop(heap)
            return (-res[0], res[1])
        
        def heaptop():
            return (-heap[0][0], heap[0][1])
        
        heappush(nums[0], 0) # maxheap
        
        next_num = nums[0]
        for i in range(1, len(nums)):

            while heaptop()[1] < i - k: # if outside range of window
                heappop()

            next_num = nums[i] + heaptop()[0]
            heappush(next_num, i)
        
        return next_num
