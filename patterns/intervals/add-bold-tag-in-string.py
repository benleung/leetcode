'''
20'

good
- first letter prefix technique

bad
misunderstand requirement
- consecutive -> combine
- two such substrings overlap -> wrap them together -> good hint for intervals
'''

from collections import defaultdict
class Solution(object):
    def addBoldTag(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        N = len(s)
        intervals = deque()
        
        # If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag?
        
        # build prefixes
        prefixes = defaultdict(list) # { "a": "abc", "1": "123"}
        for word in words:
            prefixes[word[0]].append(word)
        
        '''
        s = "abcxyz123"
        s = "abcxyz123", words = ["abc","123"]
        s = "abcxyz123", words = ["abc","xyz"]
"abcxyz123", ["abc","abcx","xyz"]
        '''
        
        def insertIntervals(start,end):
            if not intervals:
                intervals.append([start,end])
                return
            
            # merge
            if start <= intervals[-1][1] + 1: # intervals[-1][1]: end of last intervals
                # +1 is necessary[1,2] + [3,4] -> merge or not -> need to be careful
                intervals[-1][1] = max(intervals[-1][1], end)
                return
            
            # new interval
            intervals.append([start,end])
            

        # build intervals
        i = 0
        while i < N:
            ch = s[i]
            
            next_i=i
            for word in prefixes[s[i]]:
                word_len = len(word)
                
                # todo; room to optimize word comparizon
                if s[i:i+word_len] == word:
                    next_i = max(next_i,i+word_len)
            
            if next_i!=i:
                # no matches found
                insertIntervals(i, next_i-1)
            
            i += 1

        ans = []
        i = 0
        while i < N:
            if not intervals:
                ans.append(s[i:])
                break
            
            start, end = intervals.popleft()
            # unbold
            unbold = s[i:start]
            if unbold:
                ans.append(unbold)
            # bold
            ans.append("<b>{0}</b>".format(s[start:end+1]))
            
            i = end+1
        

        return "".join(ans)
