'''
11'
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        h = {}
        
        for i, ch in enumerate(order):
            h[ch] = i
        
        def cmp(left, right):
            for l, r in zip(left,right):
                if h[l]<h[r]:
                    return True
                elif h[l]>h[r]:
                    return False
            return len(left) <= len(right)
        
        for i in range(1, len(words)):
            if not ( cmp(words[i-1], words[i]) ):
                return False
            
        return True
    
    