class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        h = {}
        
        '''
        redblueredblue
        
        a: r .... n
        b: e , ed, edb, .... n
        
        P: pattern.length
        n^P * P
        '''
        
        
        
        P = len(pattern)
        S = len(s)
        words = set()   # to make sure no character maps to two different strings
        
        def dfs(p_i, s_i):
            if p_i == P and s_i == S:
                return True
            if s_i == S or p_i == P:
                return False
            
            p = pattern[p_i]
            if p in h:
                candidate = h[p]
                if candidate == s[s_i:s_i+len(candidate)]:
                    if dfs(p_i+1, s_i+len(candidate)):
                        return True
                else:
                    return False
            else:
                for candidate_len in range(1, S+1):
                    
                    candidate = s[s_i:s_i+candidate_len]  # more efficient way
                    
                    if candidate not in words:
                        words.add(candidate)
                        h[p] = candidate
                        
                        if dfs(p_i+1, s_i+len(candidate)):
                            return True
                        
                        del h[p]
                        words.remove(candidate)
                
                return False
            
        if dfs(0, 0):
            return True
        else:
            return False
        