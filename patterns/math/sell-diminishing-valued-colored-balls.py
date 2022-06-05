class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory.append(0)
        ans = 0
        width = 1    
        
        def rangeSum(a, b):
            return (a+b)*(b-a+1)//2
        
        for i in range(len(inventory)-1):
            if inventory[i]>inventory[i+1]:
                if width * (inventory[i] - inventory[i+1]) <= orders:
                    ans += rangeSum(inventory[i+1]+1, inventory[i]) * width
                    orders -= width * (inventory[i] - inventory[i+1])
                else:
                    height = orders // width
                    ans += rangeSum(inventory[i]-height+1, inventory[i]) * width
                    ans += (inventory[i]-height)* (orders%width)
                    break
                
            width += 1
            
        return ans % (10**9 + 7)
