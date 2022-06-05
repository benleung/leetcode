'''
19'30" reverse the whole process
'''
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        
        ans = deque()
        
        while deck:
            if ans:
                last = ans.pop()
                ans.appendleft(last)
            ans.appendleft(deck.pop())

        return ans
