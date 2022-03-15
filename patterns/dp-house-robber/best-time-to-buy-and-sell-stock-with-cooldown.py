'''
dp with state machine
'''

'''
with improved memorization: no unnecessary parameter
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # (cost, i) -> profit
        
        # total profit starting from index i
        # cost = float('inf') menas no stock on hand
        def backtrack(profit, cost, i):
            if (cost, i) in dp:
                return profit + dp[(cost, i)]
            
            if i >= len(prices):
                return profit
            
            if prices[i] <= cost:
                cost = prices[i] # can be bought at a lower cost, so buy here instead
                dp[(cost,i+1)] = backtrack(profit, cost, i+1) - profit
                return backtrack(profit, cost, i+1)
            else:
                # possible to gain profit here so decision to make here
                profit_to_sell_here = backtrack(profit + prices[i]-cost, float('inf'), i+2)
                
                profit_to_skip_here = backtrack(profit, cost, i+1)
                dp[(cost,i+1)] = profit_to_sell_here - profit
                
                return max(profit_to_sell_here, profit_to_skip_here)
            
        return backtrack(0, float('inf'), 0)
            

'''
with memorization but still time out
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        # total profit starting from index i
        # cost = float('inf') menas no stock on hand
        def backtrack(profit, cost, i):
            if (profit, cost, i) in dp:
                return dp[(profit, cost, i)]
            
            if i >= len(prices):
                return profit
            if prices[i] <= cost:
                cost = prices[i] # can be bought at a lower cost, so buy here instead
                dp[(profit,cost,i+1)] = backtrack(profit, cost, i+1)
                return backtrack(profit, cost, i+1)
            else:
                # possible to gain profit here so decision to make here
                dp[(profit + prices[i]-cost, float('inf'), i+2)] = profit_to_sell_here = backtrack(profit + prices[i]-cost, float('inf'), i+2)
                dp[(profit, cost, i+1)] = profit_to_skip_here = backtrack(profit, cost, i+1)
                return max(profit_to_sell_here, profit_to_skip_here)
            
        return backtrack(0, float('inf'), 0)
            

'''
recursive function
12'
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # total profit starting from index i
        # cost = float('inf') menas no stock on hand
        def backtrack(profit, cost, i):
            if i >= len(prices):
                return profit
            if prices[i] <= cost:
                cost = prices[i] # can be bought at a lower cost, so buy here instead
                return backtrack(profit, cost, i+1)
            else:
                # possible to gain profit here so decision to make here
                profit_to_sell_here = backtrack(profit + prices[i]-cost, float('inf'), i+2)
                profit_to_skip_here = backtrack(profit, cost, i+1)
                return max(profit_to_sell_here, profit_to_skip_here)
            
        return backtrack(0, float('inf'), 0)
            