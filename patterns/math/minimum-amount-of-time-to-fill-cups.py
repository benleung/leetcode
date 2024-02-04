'''
priority queue possible, but not optimized
30'


'''

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        if amount[2] >= amount[0] + amount[1]:
            # amount[2] is the majority element, hence the bottleneck here
            return amount[2]  
        
        # no bottle exists, so 2 for every round, except last round 1 or 2
        return (sum(amount)+1)//2

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        if amount[2] >= amount[0] + amount[1]:
            return amount[2]  # amount[2] is the majority element, hence the bottleneck here
        
        # optimize 2 st stone per round, 1/2 for final round
        
        return (sum(amount)+1)//2  # look at math problem
        
# 
