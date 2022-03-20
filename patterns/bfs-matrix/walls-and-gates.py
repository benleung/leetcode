'''
11'

bad:
mistake on "rooms[new_r][new_c] = dist+1"
  avoid revisited when gray
'''

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        
        # bfs from gate
        R = len(rooms)
        C = len(rooms[0])
        queue = deque()
        
        
        
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    queue.append((r,c,0))
        
        while queue:
            r, c, dist = queue.popleft()
            
            adj = [(0,1),(0,-1),(1,0),(-1,0)]
            for dr, dc in adj:
                new_r = dr+r
                new_c = dc+c
                if 0<=new_r<R and 0<=new_c<C and rooms[new_r][new_c]==INF:
                    rooms[new_r][new_c] = dist+1
                    queue.append((new_r,new_c,dist+1))
