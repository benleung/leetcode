'''
failed in contest due to inexperience in programming skills
tips is to move the bars together (which i know already but implement slow)
'''
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        heap = []
        
        for num1, num2 in zip(nums1, nums2):
            heap.append(abs(num1-num2))
        heap.sort(reverse=True)
        heap.append(0)
        k = k1 + k2

        N = len(heap)
        i = 0
        while k > 0 and i < N-1:
            count = i + 1 # number of bars to move together
            current_height = heap[i]
            height_to_move = min(k // count, heap[i] - heap[i+1]) # tricky here
            current_height -= height_to_move
            
            if current_height == 0:
                return 0
            
            k -= height_to_move*count
            if k <= count: # k == count impossible
                for j in range(count):
                    heap[j] = current_height
                for j in range(k):
                    heap[j] -= 1
                k = 0
                break
            i += 1
        
        ans = 0
        for num in heap:
            ans += num**2
        
        return ans
