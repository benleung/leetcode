'''
fail, finish after reading ans
should revise again in future

learn
- technique of filtering member
- technique of using required and self.finished and check whether all requirement is fulfilled with O(1)
- 
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        candidate = [0, inf] # [l, r]
        counter = defaultdict(int) # ch:str -> count:int
        filtered_ch = [] # [(ch, index)]
        
        dict_t = Counter(t)
        
        required = len(dict_t)
        self.finished = 0
        
        for r in range(len(s)):
            ch  = s[r]
            if ch not in dict_t:
                continue
            filtered_ch.append((ch, r))
        
        def add_member(i):
            if not (i < len(filtered_ch)):
                # out of range
                return
            
            
            
            ch, index = filtered_ch[i]
            counter[ch] += 1
            if counter[ch] == dict_t[ch]:
                self.finished += 1
        
        def remove_member(i):
            ch, index = filtered_ch[i]
            if counter[ch] == dict_t[ch]:
                self.finished -= 1
            counter[ch] -= 1

        def try_candidate(l,r):
            cur_candidate_l, cur_candidate_r = candidate
            
            
            
            if cur_candidate_r - cur_candidate_l > r - l:
                # try success
                candidate[0] = l
                candidate[1] = r
            
        l = 0
        r = 0
        add_member(0)
        while r < len(filtered_ch):
            if self.finished == required:
                try_candidate(filtered_ch[l][1], filtered_ch[r][1])
                remove_member(l)
                l += 1
            else:
                r += 1
                add_member(r)
        
        left, right = candidate
        
        return s[left:right+1] if right != inf else ""
