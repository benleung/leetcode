class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        array = []
        maxLength = max(len(a), len(b))
        for i in range(0, maxLength):
            if i + len(b) - maxLength < 0 :
                b_element = 0
            else:
                b_element = int(b[i + len(b) - maxLength])
            if i + len(a) - maxLength < 0 :
                a_element = 0
            else:
                a_element = int(a[i + len(a) - maxLength])

            array += [a_element + b_element]

        for i in reversed(range(0, maxLength)):
            if array[i] >= 2:
                array[i] -= 2
                if i - 1 >= 0:
                    array[i - 1] += 1
                else:
                    array = [1] + array
        return "".join(
            map(lambda x: str(x), array)
        )

'''
second time: 7'
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = deque()
        carry = 0
        
        A = len(a)
        B = len(b)
        
        for i in range(max(A,B)):
            left = a[A-i-1] if i < A else 0
            right = b[B-i-1] if i < B else 0
            
            nex = int(left) + int(right) + carry
            carry = nex//2
            ans.appendleft(str(nex%2))
        
        if carry == 1:
            ans.appendleft("1") 
        
        return "".join(ans)


'''
learning:
convert binary string to int by int(a, 2)
'''
