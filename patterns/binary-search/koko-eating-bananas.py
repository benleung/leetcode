'''
50' revisit on 4/11
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h > len(piles)
        min_k = math.ceil(sum(piles)/h)
        max_k = math.ceil(max(piles)/(h//len(piles))) # this is tricky and need practice
        
        self.candidate = None
        
        def hours_needed(speed):
            hour = 0
            for pile in piles:
                hour += pile//speed
                if pile % speed != 0:
                    hour += 1
            return hour 
        
        while min_k <= max_k:
            center = (min_k+max_k)//2
            hour = hours_needed(center)
            if hour > h: # no enough speed
                min_k = center + 1
            else:
                self.candidate = center  # condition is fulfilled, but can try better
                max_k = center - 1
        return self.candidate


'''
thought process
[4 3]
h=2, max_k = 4
h=3, max_k = 4 = 4 / 1
h=4, max_k = 2 = max(piles)/(h/len(piles))
'''
