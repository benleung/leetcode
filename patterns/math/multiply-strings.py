'''
29'

pass almost in one take

good
- observe my way to figure out each element value

note
- has more efficient way but not easy

careless
- else "0"

'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        MAX_DIGITS = len(num1)+len(num2)
        carry = [0]*MAX_DIGITS  # carry[0]=0
        x = [0]*MAX_DIGITS
        y = []
        
        def getNum(num, indexFromRight):
            N = len(num)
            if indexFromRight >= N:
                return 0
            return int(num[N - indexFromRight - 1])
        
        for i in range(MAX_DIGITS):
            accSum = carry[i]
            
            for j in range(i+1):
                accSum += getNum(num1, j)*getNum(num2, i-j)
            
            x[i] = accSum%10
            
            if i < MAX_DIGITS-1:
                carry[i+1] = accSum//10
        
        
        for i in range(MAX_DIGITS):
            target = x[MAX_DIGITS-i-1]
            if y == [] and target == 0:
                # remove beginning 0
                continue
            y.append(str(target))
        
        return "".join(y) if y != [] else "0"
