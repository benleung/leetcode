'''
revised on 2/23
'''
'''
9'
able to remember carry technqiue

cannot pass in one take
- edge case of last carry
- "".join expect each element to be str

'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = deque()
        carry = 0
        
        left = len(num1) - 1
        right = len(num2) - 1
        
        while left>=0 or right>=0:
            leftNum  = int(num1[left]) if left>=0 else 0
            rightNum  = int(num2[right]) if right>=0 else 0
            ans.appendleft(str((leftNum+rightNum+carry)%10))
            carry = (leftNum+rightNum+carry)//10
            left -= 1
            right -= 1
        else:
            if carry>0:
                ans.appendleft("1")
        return "".join(ans)
