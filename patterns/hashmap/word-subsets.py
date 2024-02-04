'''
11'
Counter(word).items() not confident enough
'''
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2_count = defaultdict(int) # ch -> num
        for word in words2:
            for ch, count in Counter(word).items():
                words2_count[ch] = max(count, words2_count[ch])
        
        ans = []
        
        def is_subset(word):
            counter = Counter(word)
            for ch, count_lo in words2_count.items():
                if counter[ch] < count_lo:
                    return False
            
            return True
        
        for word in words1:
            if is_subset(word):
                ans.append(word)
        
        return ans
