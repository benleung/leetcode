'''
20''
there is another way to solve
use bisect_right without additional help
'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        
        h = defaultdict(list) # ch -> [indexes]
        for i, ch in enumerate(s):
            h[ch].append(i)
        
        # return -1 if not found
        def find_index(ch, greater_than):
            arr = h[ch]
            i = bisect_right(arr, greater_than)
            if i == len(arr):
                return -1
            else:
                return arr[i]
        
        
        def is_subsequence(word):
            index = -1
            for ch in word:
                index = find_index(ch, index)
                if index == -1:
                    return False
            return True
        
        for word in words:
            if is_subsequence(word):
                ans += 1
        
        return ans
