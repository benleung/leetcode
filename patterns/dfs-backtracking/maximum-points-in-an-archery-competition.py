'''
40'

bad
being stuck at remaining arrows unused
terminal condition not detected correctly: 12 instead of 11
'''
class Solution(object):
    def maximumBobPoints(self, numArrows, aliceArrows):
        """
        :type numArrows: int
        :type aliceArrows: List[int]
        :rtype: List[int]
        """
        self.max_score = 0
        self.best_candidate = []
        self.score = 0 # current score candidate
        candidate = []
        
        # score -> depth
        def backtrack(arrows_left, score):
            if score == 12:
                # not exist score more than 11
                if self.score >= self.max_score:
                    
                    self.max_score = self.score
                    self.best_candidate = candidate[:]
                    
                    # consume the remaining arrows
                    if arrows_left > 0:
                        self.best_candidate[0] += arrows_left
                
                return
            
            # take this score
            arrow_needed = aliceArrows[score] + 1
            if arrows_left >= arrow_needed:
                self.score += score
                candidate.append(arrow_needed)
                backtrack(arrows_left-arrow_needed, score+1)
                candidate.pop()
                self.score -= score
            
            # give up this score
            candidate.append(0)
            backtrack(arrows_left, score+1)
            candidate.pop()
            
        backtrack(numArrows, 0)
        return self.best_candidate
