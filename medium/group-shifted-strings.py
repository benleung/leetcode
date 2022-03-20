'''
9'
bad
- mistake on rotatng cipher (necessary to %26)
'''
from collections import defaultdict
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list) # "aaa" : (0,0,0)  -> ["aaa"]
        
        def hash_string(string): # "aaa" -> (0,0,0)
            hashed = []
            first_ch_ord = ord(string[0])
            for ch in string:
                hashed.append((ord(ch) - first_ch_ord)%26)
            return tuple(hashed)
        
        for string in strings:
            hashmap[hash_string(string)].append(string)
        
        ans = []
        for hashkey in hashmap:
            ans.append(hashmap[hashkey])
        return ans
