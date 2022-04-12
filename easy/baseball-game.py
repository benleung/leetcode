# 9'30"
'''
prev, prevprev don't work because there can be multiple values in stack
'''
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        records  = []
        for op in ops:
            if op == "C":
                records.pop()
            elif op == "D":
                records.append(records[-1]*2)
            elif op == "+":
                records.append(records[-1] + records[-2])
            else:
                records.append(int(op))
        return sum(records)
