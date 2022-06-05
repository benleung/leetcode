'''
revisit on 4/14 4'41"
6 min after knowing the answer

imagine each coin is gain seperately one by one, modify dp in a way the best performance is gained at that set of coin
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = [float('inf')] * (amount+1)
        d[0] = 0
        for coin in coins:
            for i in range(coin, amount +1):
                d[i] = min(d[i], d[i-coin] + 1)
        
        return d[amount] if d[amount] != float('inf') else -1



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

'''
dp (bottom up)


idea of dp to represent up to amount, and d[x-y] is a smart move

but too slow
- not an effective solution because "newD = d[coin] + d[i-coin]" not effective, by coins.append(i)
- a more effective one is  to run a for loop on coins instead so that  "newD =  d[i-coin] +1"

'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = {}
        coins.sort()  # all choices
        if amount ==0:
            return 0
        for coin in coins:
            d[coin] = 1
        for i in range(1, amount+1):
            for coin in coins:
                if i > coin and i-coin in d:
                    newD = d[coin] + d[i-coin]
                    d[i] = min(d[i], newD) if i in d else newD
                    if coins[-1] != i:
                        coins.append(i)
        return d.get(amount, -1)
