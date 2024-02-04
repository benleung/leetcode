'''
revist on 12/12: 24'
37'

carelss on:
 max(right, interval[1]) ->  max(right, result[-1][1])

hesitation on converting interval to bold string
'''
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # abcxyz123
        
        def get_intervals(s, words):
            # words = ["abc","123", "aaa"]
            # prefixes = {"a": ["abc","aaa"], "1": "123"}
            
            prefixes = defaultdict(list)
            for word in words:
                if len(word) == 0:
                    continue
                prefixes[word[0]].append(word)
            
            intervals = []
            for i in range(len(s)):
                for word in prefixes[s[i]]:
                    if s[i:i+len(word)] == word:
                        intervals.append([i,i+len(word)])
            return intervals
        
        # [[0,3],[3,9]] -> [[0,9]]
        def merge_intervals(intervals):
            result = []
            
            for interval in intervals:
                if not result:
                    result.append(interval)
                else:
                    left, right = result[-1]
                    if interval[0] <= right:
                        result[-1][1] = max(right, interval[1])
                    else:
                        result.append(interval)
            
            return result
        
        # s = "abcxyz123"
        # [[0,3],[6,9]]
        # "<b>abc</b>xyz<b>123</b>"
        def intervals_to_boldstring(intervals):
            pointer = 0
            result = []
            for i in range(len(s)):
                interval = intervals[pointer] if pointer < len(intervals) else None
                if interval and i == interval[0]:
                    result.append("<b>")
                if interval and i == interval[1]:
                    result.append("</b>")
                    pointer += 1
                result.append(s[i])

            if interval and len(s) == interval[1]:
                result.append("</b>")
            
            return "".join(result)
        
        # [[0,3],[6,9]] -> end not included
        intervals = get_intervals(s, words)
        
        intervals = merge_intervals(intervals)
        
        return intervals_to_boldstring(intervals)

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
