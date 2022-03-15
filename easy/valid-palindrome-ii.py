'''
13' recursion
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        
        def isValid(left, right, one_more_chance = True):
            while left < right:
                if s[left] != s[right]:
                    if one_more_chance:
                        return isValid(left, right-1, False) or isValid(left+1, right, False)
                    else:
                        return False
                    
                else:
                    left += 1
                    right -= 1
            else:
                return True
        
        return isValid(0, len(s)-1)
