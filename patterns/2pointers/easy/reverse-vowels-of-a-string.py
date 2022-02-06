'''
17' 
- about 2' to understand q

bad
- first tried writing for ... in zip, but know it doesn't work in the middle (forget 2 pointer method)
- forget capital letter cases (need to read question in better details)

learnt
- list(s)
- s[0] is not working
- list(s) can convert string to array of ch

'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return s
        word = list(s)
        h = [
            'a' , 
            'e' , 
            'i' , 
            'o' , 
            'u' , 
            'A',
            'E',
            'I',
            'O',
            'U'
        ]
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and s[left] not in h:
                left += 1
            while left < right and s[right] not in h:
                right -= 1
            if left < right:
                tmp = word[left]
                word[left] = word[right]
                word[right] = tmp
                left += 1
                right -= 1
        return "".join(word)
            