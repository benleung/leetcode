'''
20'
decision making during greedy (no sure it's good for future -> should use dp)
'''
class Solution(object):
    def stoneGame(self, piles):
        N = len(piles)
        
        if N <= 2:
            return True
        
        dp = {} # (i,j) -> int # max alice can get 
        
        def max_alice(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            is_alice_turn = (N - (j-i) ) % 2 == 1
            multiplier = 1 if is_alice_turn else -1
            
            if i == j:
                dp[(i,j)] = multiplier*piles[i]
            else:
                dp[(i,j)] = max( multiplier*piles[i] + max_alice(i+1,j), multiplier*piles[j] + max_alice(i,j-1) )
            return dp[(i,j)]
            
        return max_alice(0,N-1) > 0
