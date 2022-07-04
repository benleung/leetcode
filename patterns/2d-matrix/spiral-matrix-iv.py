'''
10'
'''
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1]*n for _ in range(m)]
        state = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]
        statePointer = 0
        (di, dj) = state[0]
        i = 0
        j = 0
        
        while head:
            val = head.val
            matrix[i][j] = val
            
            if di+i==m or dj+j==n or matrix[di+i][dj+j] != -1:
                statePointer = (statePointer+1)%4
                (di, dj) = state[statePointer%4]
            i, j = di+i, dj+j
            
            head = head.next
        
        return matrix
