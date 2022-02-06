'''
1 hr

'''


# wrong answer (greedy algorithm doesn't work)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.coins.sort(reverse=True)
        print(self.coins)
        return self.dfs(amount, 0)
        
    def dfs(self, amount, count):
        if amount == 0:
            return count
        if self.coins[-1]>amount:  # actually unnecessary
            return -1
        
        
        for coin in self.coins:
            if amount - coin >=0:
                result = self.dfs(amount - coin, 1+count)
                if result != -1:
                    return result
        else:
            return -1

# correct but too slow
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.coins.sort(reverse=True)
        self.dp = {} #amount: count
        
        
        print(self.coins)
        return self.dfs(amount, 0)
        
    def dfs(self, idxCoin, amount):
        if amount == 0:
            return 0
        if idxCoin < len(self.coins) and amount > 0:
            coin = self.coins[idxCoin]
            maxCount = amount//coin
            minCost = float('inf')

            for i in range(maxCount+1):
                # explore all possibilities
                if amount >= i*coin:
                    result = self.dfs(idxCoin+1, amount-i*coin)
                    if result != -1:
                        minCost = min(result+i, minCost)
            return minCost if minCost != float('inf') else -1
        return -1
        
# dp (top down)
'''
public class Solution {

  public int coinChange(int[] coins, int amount) {
    if (amount < 1) return 0;
    return coinChange(coins, amount, new int[amount]);  # new int[amount] is dp, correspond to F(S) in notion note
  }

  private int coinChange(int[] coins, int rem, int[] count) {
    if (rem < 0) return -1;
    if (rem == 0) return 0;
    if (count[rem - 1] != 0) return count[rem - 1];
    int min = Integer.MAX_VALUE;
    for (int coin : coins) {
      int res = coinChange(coins, rem - coin, count);
      if (res >= 0 && res < min)   # key here on how to add 
        min = 1 + res;
    }
    count[rem - 1] = (min == Integer.MAX_VALUE) ? -1 : min;
    return count[rem - 1];
  }
}

'''

# dp (bottom up)
