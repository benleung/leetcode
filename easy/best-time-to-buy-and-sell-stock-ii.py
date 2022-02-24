'''
13'
feel like easy
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                # decreasing
                profit += prices[i] - prices[i-1]
        
        return profit

'''
8'

comment
easy when visualized in graph
the name is "Peak Valley Approach"
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur = prices[0]
        for i in range(1, len(prices)):
            profit += max(0, prices[i]-cur)
            cur = prices[i]
            
        
        return profit
