class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0 and num != 1:
            if num %2 == 1:
                steps += 1
            num //= 2
            steps += 1
        if num == 1:
            steps += 1
        return steps
