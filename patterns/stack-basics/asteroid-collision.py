'''
17'
include whiteboarding
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # [5, 10, -5]
        #     left right
        # [5, 10]
        
        '''
        [5, -1, -2, 10] <- 10 (coutn from right, positive)never explode
        
        
        [5, -1, -2, 10]
        sol 
        rightStack (right pop first) = [-2, -1]
        if 5 > -1:
          rightStack.pop()
        
        [5, 20, -1, -2, 10]
            _
        sol 10
        
        right = []
        # left stack not require
        
        '''
        sol = deque()
        right = deque()
        
        for a in asteroids[::-1]:      
            if a > 0:
                while right:
                    if abs(right[0]) < a:
                        right.popleft()
                    elif abs(right[0]) == a:
                        right.popleft()
                        break
                    else:
                        break # left exploded, dont append
                else:
                    sol.appendleft(a)
            else:
                right.appendleft(a)
        
        return right + sol
