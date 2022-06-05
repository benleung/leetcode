class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = []
        if numRows == 1:
            return s
        
        def append(index):
            if 0<=index<len(s):
                ans.append(s[index])
        
        for row in range(numRows):
            i = 0
            x = 0
            while x-row < len(s):
                x = 2*i*(numRows-1)
                if row == 0 or row == numRows - 1:
                    append(x+row)
                else:
                    append(x-row)
                    append(x+row)
                
                
                i += 1
        return "".join(ans)
