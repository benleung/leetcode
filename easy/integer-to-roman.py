'''
20' solved by simply walk through and observation
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        ans = deque()
        
        def digitToRoman(depth,i):
            romans = [
                ['I', 'V', 'X'],
                ['X', 'L', 'C'],
                ['C', 'D', 'M'],
                ['M']
            ]
            roman = romans[depth]
            if i ==0:
                return ""
            elif 1<=i<=3:
                return roman[0] * i
            elif i==4:
                return roman[0] + roman[1]
            elif i==5:
                return roman[1]
            elif 6<=i<=8:
                return roman[1] + roman[0]*(i-5)
            else:#9
                return roman[0] + roman[2]
            
        
        depth = 0
        while num > 0:
            digit = num % 10
            num //= 10
            ans.appendleft(digitToRoman(depth,digit))
            depth += 1
            
        return "".join(ans)
