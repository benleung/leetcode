'''
think of the last seen skill myself
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        start=0
        h = {} # lastSeen
        for i,c in enumerate(s):
            if c in h and h[c]>=start:
                # duplicate is detect
                start = h[c] + 1
            else:
                # no duplicate, register new character
                maxCount = max(maxCount, i-start+1)
            h[c] = i
        return maxCount
