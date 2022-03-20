'''
10' if knowing answer in advance
'''
from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ch_count_in_window = defaultdict(int)
        l = 0
        N  = len(s)
        ans = 0
        for r in range(N):
            ch_count_in_window[s[r]] += 1
            
            window_size = r-l+1
            candidate_size = max(ch_count_in_window.values()) # decide a candidate (ch with max freq)
            non_candidate_size = window_size - candidate_size
            
            # k constrainst doesn't allow, should shrink
            if non_candidate_size > k:
                ch_count_in_window[s[l]] -= 1
                l += 1
            
            # recalculate window size
            window_size = r-l+1
            
            ans = max(ans, window_size)
        return ans

'''
backtracking solution
too slow
'''
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        N  = len(s)
        
        self.max_substring_length = 1        
        
        def backtrack(i, k, candidate, candidate_length):
            self.max_substring_length = max(self.max_substring_length, candidate_length)
            
            # terminal
            if i >= N:
                
                # can be more efficient
                return
            
            # valid here (try record)
            
            ch = s[i]
            if ch == candidate:
                # keep
                backtrack(i+1, k, ch, candidate_length + 1)
            
            else:  # ch != candidate
                # change to candidate
                if candidate != None and k>0:
                    backtrack(i+1, k-1, candidate, candidate_length + 1)
                
                # keep
                backtrack(i+1, k, ch, 1)

            # try a new candidate (same as character after)
            if k>0 and i+1 < N and  s[i+1] != ch:
                backtrack(i+1, k-1, s[i+1], 1)

        backtrack(0, k, None, 0)
        
        return self.max_substring_length
