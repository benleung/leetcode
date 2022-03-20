'''
20'
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        directions = ["R", "D","L","U"]
        i = 0
        
        N = len(matrix)
        M = len(matrix[0])
        
        r = M-1
        l = 0
        d = N-1
        u = 1
        
        ans = []
        
        y = 0
        x = 0
        while True:
            
            # direction update
            direction = directions[i%4]
            if direction == "R":
                if r == x:
                    i += 1
                    r -= 1
            elif direction == "L":
                if l == x:
                    i += 1
                    l += 1
            elif direction == "D":
                if d == y:
                    i += 1
                    d -= 1
            elif direction == "U":
                if u == y:
                    i += 1
                    u += 1
            direction = directions[i%4]
            
            ans.append(matrix[y][x])
            if len(ans) == N*M:
                return ans
            
            if direction == "R":
                x = x +1
            elif direction == "L":
                x = x -1
            elif direction == "D":
                y = y +1
            elif direction == "U":
                y = y -1
