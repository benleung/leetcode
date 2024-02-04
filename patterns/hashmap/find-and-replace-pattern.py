'''
8' understand this is 1-1 map problem


'''
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        ans = []
        
        def isMatchPattern(word):
            wp = {}
            pw = {}
            
            for w_ch, p_ch in zip(word, pattern):
                if p_ch in pw and pw[p_ch] != w_ch:
                    return False
                
                if w_ch in wp and wp[w_ch] != p_ch:
                    return False
                
                pw[p_ch]= w_ch
                wp[w_ch] = p_ch
            else:
                return True
        
        for word in words:
            if isMatchPattern(word):
                ans.append(word)
        
        return ans

'''
after looking at solution, (m1[w], m2[p]) != (p, w) is a neat way
'''
