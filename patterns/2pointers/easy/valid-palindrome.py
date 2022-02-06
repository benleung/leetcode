class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = ''.join(x for x in s if x.isalnum())
        
        middle = int(len(string)/2)
        for i in range(0, middle):
            if string[i].lower() != string[len(string)-i-1].lower():
                return False
        return True
