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