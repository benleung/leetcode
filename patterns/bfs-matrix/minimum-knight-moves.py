'''
30'

'''
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        up = {
            (-2, 1), (-1, 2), (1, 2), (2, 1) # x, y
        }
        down = {
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        }
        right = {
            (1, -2), (2, -1), (1, 2), (2, 1)
        }
        left = {
            (-1, -2), (-2, -1), (-1, 2), (-2, 1)
        }

        visited = set()
        
        queue = deque([(0, 0, 0)]) # (new_x, new_y, move)
        visited.add((0,0))
        
        while queue:
            new_x, new_y, move = queue.popleft()
            if new_x == x and new_y == y:
                return move
            
            neighbors = set()
            if x > new_x:
                neighbors |= right
            if x < new_x:
                neighbors |= left
            if y > new_y:
                neighbors |= up
            if y < new_x:
                neighbors |= down
            
            for dx, dy in neighbors:
                neighbor_x = new_x + dx
                neighbor_y = new_y + dy
                if (neighbor_x, neighbor_y) not in visited:
                    visited.add( (neighbor_x, neighbor_y) )
                    queue.append((neighbor_x, neighbor_y, move+1))
        