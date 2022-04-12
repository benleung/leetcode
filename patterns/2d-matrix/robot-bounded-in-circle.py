'''
40'
think of the answer myself
observe the patterns carefully
theory of direction rotating
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir_counter = 0
        directions = [
            (0,1), (1,0), (0,-1), (-1,0)
        ] # x, y
        x = 0
        y = 0
        for instruction in instructions:
            if instruction == "G":
                dx, dy = directions[dir_counter%4]
                x, y = dx + x, dy + y
            elif instruction == "L":
                dir_counter -= 1
            elif instruction == "R":
                dir_counter += 1
        
        dir_counter = dir_counter%4
        if dir_counter == 0:
            return (x,y) == (0,0)
        return True
        