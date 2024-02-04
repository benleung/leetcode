'''
wall problem: similar to asteroid, stack is good for this kind of question
'''
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        stack = deque()
        N = len(start)
        for i in range(N):
            if start[i] == "L" or start[i] == 'R':
                stack.append((start[i],i))
        
        for i in range(N):
            if target[i] == "L" or target[i] == 'R':
                if len(stack) == 0:
                    return False
                direction, index = stack.popleft()
                if target[i] == 'L':
                    if not (direction == 'L' and i <= index):
                        return False
                elif target[i] == 'R':
                    if not (direction == 'R' and i >= index):
                        return False
        else:
            if len(stack) != 0:
                return False
                    
        return True
        


# troublesome solution
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        startLs = []
        startRs = []
        
        wallLs = []
        
        for i, ch in enumerate(start):
            if ch == 'L':
                startLs.append(i)
            elif ch == 'R':
                startRs.append(i)
                
        targetLs = []
        targetRs = []
        for i, ch in enumerate(target):
            if ch == 'L':
                targetLs.append(i)
            elif ch == 'R':
                targetRs.append(i)    
        
        wallLs = []
        r_ptr = -1
        for val in startLs:
            wall = startRs[r_ptr] if r_ptr != -1 else -1
            
            # wall < val is always
            while r_ptr+1 < len(startRs) and not (val < startRs[r_ptr+1]) :
                r_ptr += 1
                wall = startRs[r_ptr]
            wallLs.append(wall)
        print(wallLs)
        
        if len(startLs) != len(targetLs) or len(startRs) != len(targetRs):
            return False
        
        def can_move_L(src, dest, i):
            # impossible to be bordered by L
            return dest > wallLs[i]
        
        # move L
        for i in range(len(startLs)):
            if startLs[i] == targetLs[i]:
                continue
            elif targetLs[i] > startLs[i]:
                return False
            else:
                #move
                if can_move_L(startLs[i], targetLs[i], i):
                    startLs[i] = targetLs[i]
                else:
                    return False
                

        wallRs = [None]*len(startRs)
        r_ptr = len(startLs)
        for i in range(len(startRs)-1, -1, -1):
            val = startRs[i]
            wall = startLs[r_ptr] if r_ptr != len(startLs) else len(start)
            
            # val < wall is always
            while r_ptr-1 >= 0 and not (startLs[r_ptr-1] < val):
                r_ptr -= 1
                wall = startLs[r_ptr]
            wallRs[i] = wall
        print(wallRs)
        
        def can_move_R(src, dest, i):
            # impossible to be bordered by L
            return dest < wallRs[i]
        
        # move R
        for i in range(len(startRs)-1, -1, -1):
            if startRs[i] == targetRs[i]:
                continue
            elif targetRs[i] < startRs[i]:
                return False
            else:
                #move
                if not can_move_R(startRs[i], targetRs[i], i):
                    return False
        
        
        return True
        