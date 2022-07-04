class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = [0]*(k+1) # use i left cards -> left[i]
        
        for i in range(1, k+1):
            left[i] = left[i-1] + cardPoints[i-1]
        
        ans = 0
        right_pts = 0
        N = len(cardPoints)
        for right_cards in range(k+1):
            left_cards = k-right_cards
            right_pts += cardPoints[N-right_cards] if right_cards > 0 else 0
            
            ans = max(ans, left[left_cards] + right_pts)
            
        return ans
